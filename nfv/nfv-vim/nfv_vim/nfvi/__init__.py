#
# Copyright (c) 2015-2016 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#
# flake8: noqa
#
import nfv_vim.nfvi.api
import nfv_vim.nfvi.objects

from ._nfvi_defs import NFVI_ERROR_CODE
from ._nfvi_identity_module import nfvi_get_tenants
from ._nfvi_guest_module import nfvi_guest_services_create
from ._nfvi_guest_module import nfvi_guest_services_set
from ._nfvi_guest_module import nfvi_guest_services_delete
from ._nfvi_guest_module import nfvi_guest_services_query
from ._nfvi_guest_module import nfvi_guest_services_vote
from ._nfvi_guest_module import nfvi_guest_services_notify
from ._nfvi_guest_module import nfvi_register_host_services_query_callback
from ._nfvi_guest_module import nfvi_register_guest_services_query_callback
from ._nfvi_guest_module import nfvi_register_guest_services_state_notify_callback
from ._nfvi_guest_module import nfvi_register_guest_services_alarm_notify_callback
from ._nfvi_guest_module import nfvi_register_guest_services_action_notify_callback
from ._nfvi_infrastructure_module import nfvi_get_system_info
from ._nfvi_infrastructure_module import nfvi_get_system_state
from ._nfvi_infrastructure_module import nfvi_get_hosts
from ._nfvi_infrastructure_module import nfvi_get_host
from ._nfvi_infrastructure_module import nfvi_get_upgrade
from ._nfvi_infrastructure_module import nfvi_upgrade_start
from ._nfvi_infrastructure_module import nfvi_upgrade_activate
from ._nfvi_infrastructure_module import nfvi_upgrade_complete
from ._nfvi_infrastructure_module import nfvi_create_host_services
from ._nfvi_infrastructure_module import nfvi_delete_host_services
from ._nfvi_infrastructure_module import nfvi_enable_host_services
from ._nfvi_infrastructure_module import nfvi_disable_host_services
from ._nfvi_infrastructure_module import nfvi_query_host_services
from ._nfvi_infrastructure_module import nfvi_notify_host_services_enabled
from ._nfvi_infrastructure_module import nfvi_notify_host_services_disabled
from ._nfvi_infrastructure_module import nfvi_notify_host_services_disable_extend
from ._nfvi_infrastructure_module import nfvi_notify_host_services_disable_failed
from ._nfvi_infrastructure_module import nfvi_notify_host_services_deleted
from ._nfvi_infrastructure_module import nfvi_notify_host_services_delete_failed
from ._nfvi_infrastructure_module import nfvi_notify_host_enabled
from ._nfvi_infrastructure_module import nfvi_notify_host_disabled
from ._nfvi_infrastructure_module import nfvi_notify_host_failed
from ._nfvi_infrastructure_module import nfvi_lock_host
from ._nfvi_infrastructure_module import nfvi_unlock_host
from ._nfvi_infrastructure_module import nfvi_reboot_host
from ._nfvi_infrastructure_module import nfvi_upgrade_host
from ._nfvi_infrastructure_module import nfvi_swact_from_host
from ._nfvi_infrastructure_module import nfvi_get_alarms
from ._nfvi_infrastructure_module import nfvi_get_logs
from ._nfvi_infrastructure_module import nfvi_get_alarm_history
from ._nfvi_infrastructure_module import nfvi_register_host_add_callback
from ._nfvi_infrastructure_module import nfvi_register_host_action_callback
from ._nfvi_infrastructure_module import nfvi_register_host_state_change_callback
from ._nfvi_infrastructure_module import nfvi_register_host_get_callback
from ._nfvi_infrastructure_module import nfvi_register_host_upgrade_callback
from ._nfvi_infrastructure_module import nfvi_register_host_notification_callback
from ._nfvi_image_module import nfvi_get_images
from ._nfvi_image_module import nfvi_create_image
from ._nfvi_image_module import nfvi_delete_image
from ._nfvi_image_module import nfvi_update_image
from ._nfvi_image_module import nfvi_get_image
from ._nfvi_block_storage_module import nfvi_get_volumes
from ._nfvi_block_storage_module import nfvi_create_volume
from ._nfvi_block_storage_module import nfvi_delete_volume
from ._nfvi_block_storage_module import nfvi_update_volume
from ._nfvi_block_storage_module import nfvi_get_volume
from ._nfvi_block_storage_module import nfvi_get_volume_snapshots
from ._nfvi_network_module import nfvi_get_networks
from ._nfvi_network_module import nfvi_create_network
from ._nfvi_network_module import nfvi_update_network
from ._nfvi_network_module import nfvi_delete_network
from ._nfvi_network_module import nfvi_get_network
from ._nfvi_network_module import nfvi_create_subnet
from ._nfvi_network_module import nfvi_update_subnet
from ._nfvi_network_module import nfvi_delete_subnet
from ._nfvi_network_module import nfvi_get_subnet
from ._nfvi_network_module import nfvi_get_subnets
from ._nfvi_compute_module import nfvi_get_host_aggregates
from ._nfvi_compute_module import nfvi_get_hypervisors
from ._nfvi_compute_module import nfvi_get_hypervisor
from ._nfvi_compute_module import nfvi_get_instance_types
from ._nfvi_compute_module import nfvi_create_instance_type
from ._nfvi_compute_module import nfvi_delete_instance_type
from ._nfvi_compute_module import nfvi_get_instance_type
from ._nfvi_compute_module import nfvi_get_instance_groups
from ._nfvi_compute_module import nfvi_get_instances
from ._nfvi_compute_module import nfvi_create_instance
from ._nfvi_compute_module import nfvi_live_migrate_instance
from ._nfvi_compute_module import nfvi_cold_migrate_instance
from ._nfvi_compute_module import nfvi_cold_migrate_confirm_instance
from ._nfvi_compute_module import nfvi_cold_migrate_revert_instance
from ._nfvi_compute_module import nfvi_resize_instance
from ._nfvi_compute_module import nfvi_resize_confirm_instance
from ._nfvi_compute_module import nfvi_resize_revert_instance
from ._nfvi_compute_module import nfvi_evacuate_instance
from ._nfvi_compute_module import nfvi_reboot_instance
from ._nfvi_compute_module import nfvi_rebuild_instance
from ._nfvi_compute_module import nfvi_fail_instance
from ._nfvi_compute_module import nfvi_pause_instance
from ._nfvi_compute_module import nfvi_unpause_instance
from ._nfvi_compute_module import nfvi_suspend_instance
from ._nfvi_compute_module import nfvi_resume_instance
from ._nfvi_compute_module import nfvi_start_instance
from ._nfvi_compute_module import nfvi_stop_instance
from ._nfvi_compute_module import nfvi_delete_instance
from ._nfvi_compute_module import nfvi_get_instance
from ._nfvi_compute_module import nfvi_reject_instance_action
from ._nfvi_compute_module import nfvi_register_instance_delete_callback
from ._nfvi_compute_module import nfvi_register_instance_state_change_callback
from ._nfvi_compute_module import nfvi_register_instance_action_change_callback
from ._nfvi_compute_module import nfvi_register_instance_action_callback
from ._nfvi_sw_mgmt_module import nfvi_sw_mgmt_query_updates
from ._nfvi_sw_mgmt_module import nfvi_sw_mgmt_query_hosts
from ._nfvi_sw_mgmt_module import nfvi_sw_mgmt_update_host
from ._nfvi_sw_mgmt_module import nfvi_sw_mgmt_update_hosts
from ._nfvi_module import nfvi_initialize, nfvi_finalize
