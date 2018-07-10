#
# Copyright (c) 2015-2016 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#
import json

from six.moves.urllib.error import HTTPError
from six.moves.urllib.error import URLError
from six.moves.urllib.request import Request
from six.moves.urllib.request import urlopen

from nfv_common import debug

from nfv_plugins.nfvi_plugins.openstack.objects import Directory
from nfv_plugins.nfvi_plugins.openstack.objects import OPENSTACK_SERVICE
from nfv_plugins.nfvi_plugins.openstack.objects import Token

DLOG = debug.debug_get_logger('nfv_plugins.nfvi_plugins.openstack')


def get_token(directory):
    """
    Ask OpenStack for a token
    """
    try:
        if directory.auth_uri is None:
            url = ("%s://%s:%s/v3/auth/tokens" % (directory.auth_protocol,
                                                  directory.auth_host,
                                                  directory.auth_port))
        else:
            url = directory.auth_uri + "/v3/auth/tokens"

        request_info = Request(url)
        request_info.add_header("Content-Type", "application/json")
        request_info.add_header("Accept", "application/json")

        if directory.auth_password is None:
            import keyring
            password = keyring.get_password('CGCS', directory.auth_username)
        else:
            password = directory.auth_password

        payload = json.dumps(
            {"auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": directory.auth_username,
                            "password": password,
                            "domain": {"name": directory.auth_user_domain_name}
                        }
                    }
                },
                "scope": {
                    "project": {
                        "name": directory.auth_project,
                        "domain": {"name": directory.auth_project_domain_name}
                    }}}})
        request_info.add_data(payload)

        request = urlopen(request_info)
        # Identity API v3 returns token id in X-Subject-Token
        # response header.
        token_id = request.info().getheader('X-Subject-Token')
        response = json.loads(request.read())
        request.close()
        return Token(response, directory, token_id)

    except HTTPError as e:
        DLOG.error("%s" % e)
        return None

    except URLError as e:
        DLOG.error("%s" % e)
        return None


def get_directory(config):
    """
    Get directory information from the given configuration
    """
    openstack_info = config.CONF.get('openstack', None)
    if openstack_info is not None:
        auth_uri = openstack_info.get('authorization_uri', None)
    else:
        auth_uri = None

    directory = Directory(config.CONF['openstack']['authorization_protocol'],
                          config.CONF['openstack']['authorization_ip'],
                          config.CONF['openstack']['authorization_port'],
                          config.CONF['openstack']['tenant'],
                          config.CONF['openstack']['username'],
                          config.CONF['openstack']['password'],
                          config.CONF['openstack']['user_domain_name'],
                          config.CONF['openstack']['project_domain_name'],
                          auth_uri)

    for service in OPENSTACK_SERVICE:
        service_info = config.CONF.get(service, None)
        if service_info is not None:
            region_name = service_info.get('region_name', None)
            service_name = service_info.get('service_name', None)
            service_type = service_info.get('service_type', None)
            endpoint_type = service_info.get('endpoint_type', None)
            endpoint_override = service_info.get('endpoint_override', None)
            endpoint_disabled = service_info.get('endpoint_disabled', False)

            if endpoint_disabled in ['Yes', 'yes', 'Y', 'y', 'True', 'true',
                                     'T', 't', '1']:
                endpoint_disabled = True
            else:
                endpoint_disabled = False

            if (((region_name is not None and service_name is not None and
                  service_type is not None and endpoint_type is not None) or
                 endpoint_override is not None) and not endpoint_disabled):

                directory.set_service_info(service, region_name, service_name,
                                           service_type, endpoint_type,
                                           endpoint_override)

    return directory
