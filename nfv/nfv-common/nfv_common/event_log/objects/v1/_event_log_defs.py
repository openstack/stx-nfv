#
# Copyright (c) 2015-2016 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#
import six

from nfv_common.helpers import Constant
from nfv_common.helpers import Constants
from nfv_common.helpers import Singleton


@six.add_metaclass(Singleton)
class _EventId(Constants):
    """
    Event Type Constants
    """
    UNKNOWN = Constant('unknown')
    MULTI_NODE_RECOVERY_MODE_ENTER = Constant('multi-node-recovery-enter')
    MULTI_NODE_RECOVERY_MODE_EXIT = Constant('multi-node-recovery-exit')
    HOST_SERVICES_ENABLED = Constant('host-services-enabled')
    HOST_SERVICES_DISABLED = Constant('host-services-disabled')
    HOST_SERVICES_FAILED = Constant('host-services-failed')
    HYPERVISOR_STATE_CHANGE = Constant('hypervisor-state-change')
    INSTANCE_RENAMED = Constant('instance-renamed')
    INSTANCE_ENABLED = Constant('instance-enabled')
    INSTANCE_FAILED = Constant('instance-failed')
    INSTANCE_SCHEDULING_FAILED = Constant('instance-scheduling-failed')
    INSTANCE_CREATE_BEGIN = Constant('instance-create-begin')
    INSTANCE_CREATING = Constant('instance-creating')
    INSTANCE_CREATE_REJECTED = Constant('instance-create-rejected')
    INSTANCE_CREATE_CANCELLED = Constant('instance-create-cancelled')
    INSTANCE_CREATE_FAILED = Constant('instance-create-failed')
    INSTANCE_CREATED = Constant('instance-created')
    INSTANCE_DELETE_BEGIN = Constant('instance-delete-begin')
    INSTANCE_DELETING = Constant('instance-deleting')
    INSTANCE_DELETE_REJECTED = Constant('instance-delete-rejected')
    INSTANCE_DELETE_CANCELLED = Constant('instance-delete-cancelled')
    INSTANCE_DELETE_FAILED = Constant('instance-delete-failed')
    INSTANCE_DELETED = Constant('instance-deleted')
    INSTANCE_PAUSE_BEGIN = Constant('instance-pause-begin')
    INSTANCE_PAUSING = Constant('instance-pausing')
    INSTANCE_PAUSE_REJECTED = Constant('instance-pause-rejected')
    INSTANCE_PAUSE_CANCELLED = Constant('instance-pause-cancelled')
    INSTANCE_PAUSE_FAILED = Constant('instance-pause-failed')
    INSTANCE_PAUSED = Constant('instance-paused')
    INSTANCE_UNPAUSE_BEGIN = Constant('instance-unpause-begin')
    INSTANCE_UNPAUSING = Constant('instance-unpausing')
    INSTANCE_UNPAUSE_REJECTED = Constant('instance-unpause-rejected')
    INSTANCE_UNPAUSE_CANCELLED = Constant('instance-unpause-cancelled')
    INSTANCE_UNPAUSE_FAILED = Constant('instance-unpause-failed')
    INSTANCE_UNPAUSED = Constant('instance-unpaused')
    INSTANCE_SUSPEND_BEGIN = Constant('instance-suspend-begin')
    INSTANCE_SUSPENDING = Constant('instance-suspending')
    INSTANCE_SUSPEND_REJECTED = Constant('instance-suspend-rejected')
    INSTANCE_SUSPEND_CANCELLED = Constant('instance-suspend-cancelled')
    INSTANCE_SUSPEND_FAILED = Constant('instance-suspend-failed')
    INSTANCE_SUSPENDED = Constant('instance-suspended')
    INSTANCE_RESUME_BEGIN = Constant('instance-resume-begin')
    INSTANCE_RESUMING = Constant('instance-resuming')
    INSTANCE_RESUME_REJECTED = Constant('instance-resume-rejected')
    INSTANCE_RESUME_CANCELLED = Constant('instance-resume-cancelled')
    INSTANCE_RESUME_FAILED = Constant('instance-resume-failed')
    INSTANCE_RESUMED = Constant('instance-resumed')
    INSTANCE_START_BEGIN = Constant('instance-start-begin')
    INSTANCE_STARTING = Constant('instance-starting')
    INSTANCE_START_REJECTED = Constant('instance-start-rejected')
    INSTANCE_START_CANCELLED = Constant('instance-start-cancelled')
    INSTANCE_START_FAILED = Constant('instance-start-failed')
    INSTANCE_STARTED = Constant('instance-started')
    INSTANCE_STOP_BEGIN = Constant('instance-stop-begin')
    INSTANCE_STOPPING = Constant('instance-stopping')
    INSTANCE_STOP_REJECTED = Constant('instance-stop-rejected')
    INSTANCE_STOP_CANCELLED = Constant('instance-stop-cancelled')
    INSTANCE_STOP_FAILED = Constant('instance-stop-failed')
    INSTANCE_STOPPED = Constant('instance-stopped')
    INSTANCE_LIVE_MIGRATE_BEGIN = Constant('instance-live-migrate-begin')
    INSTANCE_LIVE_MIGRATING = Constant('instance-live-migrating')
    INSTANCE_LIVE_MIGRATE_REJECTED = Constant('instance-live-migrate-rejected')
    INSTANCE_LIVE_MIGRATE_CANCELLED = Constant('instance-live-migrate-cancelled')
    INSTANCE_LIVE_MIGRATE_FAILED = Constant('instance-live-migrate-failed')
    INSTANCE_LIVE_MIGRATED = Constant('instance-live-migrated')
    INSTANCE_COLD_MIGRATE_BEGIN = Constant('instance-cold-migrate-begin')
    INSTANCE_COLD_MIGRATING = Constant('instance-cold-migrating')
    INSTANCE_COLD_MIGRATE_REJECTED = Constant('instance-cold-migrate-rejected')
    INSTANCE_COLD_MIGRATE_CANCELLED = Constant('instance-cold-migrate-cancelled')
    INSTANCE_COLD_MIGRATE_FAILED = Constant('instance-cold-migrate-failed')
    INSTANCE_COLD_MIGRATED = Constant('instance-cold-migrated')
    INSTANCE_COLD_MIGRATE_CONFIRM_BEGIN = Constant('instance-cold-migrate-confirm-begin')
    INSTANCE_COLD_MIGRATE_CONFIRMING = Constant('instance-cold-migrate-confirming')
    INSTANCE_COLD_MIGRATE_CONFIRM_REJECTED = Constant('instance-cold-migrate-confirm-rejected')
    INSTANCE_COLD_MIGRATE_CONFIRM_CANCELLED = Constant('instance-cold-migrate-confirm-cancelled')
    INSTANCE_COLD_MIGRATE_CONFIRM_FAILED = Constant('instance-cold-migrate-confirm-failed')
    INSTANCE_COLD_MIGRATE_CONFIRMED = Constant('instance-cold-migrate-confirmed')
    INSTANCE_COLD_MIGRATE_REVERT_BEGIN = Constant('instance-cold-migrate-revert-begin')
    INSTANCE_COLD_MIGRATE_REVERTING = Constant('instance-cold-migrate-reverting')
    INSTANCE_COLD_MIGRATE_REVERT_REJECTED = Constant('instance-cold-migrate-revert-rejected')
    INSTANCE_COLD_MIGRATE_REVERT_CANCELLED = Constant('instance-cold-migrate-revert-cancelled')
    INSTANCE_COLD_MIGRATE_REVERT_FAILED = Constant('instance-cold-migrate-revert-failed')
    INSTANCE_COLD_MIGRATE_REVERTED = Constant('instance-cold-migrate-reverted')
    INSTANCE_EVACUATE_BEGIN = Constant('instance-evacuate-begin')
    INSTANCE_EVACUATING = Constant('instance-evacuating')
    INSTANCE_EVACUATE_REJECTED = Constant('instance-evacuate-rejected')
    INSTANCE_EVACUATE_CANCELLED = Constant('instance-evacuate-cancelled')
    INSTANCE_EVACUATE_FAILED = Constant('instance-evacuate-failed')
    INSTANCE_EVACUATED = Constant('instance-evacuated')
    INSTANCE_REBOOT_BEGIN = Constant('instance-reboot-begin')
    INSTANCE_REBOOTING = Constant('instance-rebooting')
    INSTANCE_REBOOT_REJECTED = Constant('instance-reboot-rejected')
    INSTANCE_REBOOT_CANCELLED = Constant('instance-reboot-cancelled')
    INSTANCE_REBOOT_FAILED = Constant('instance-reboot-failed')
    INSTANCE_REBOOTED = Constant('instance-rebooted')
    INSTANCE_REBUILD_BEGIN = Constant('instance-rebuild-begin')
    INSTANCE_REBUILDING = Constant('instance-rebuilding')
    INSTANCE_REBUILD_REJECTED = Constant('instance-rebuild-rejected')
    INSTANCE_REBUILD_CANCELLED = Constant('instance-rebuild-cancelled')
    INSTANCE_REBUILD_FAILED = Constant('instance-rebuild-failed')
    INSTANCE_REBUILT = Constant('instance-rebuilt')
    INSTANCE_RESIZE_BEGIN = Constant('instance-resize-begin')
    INSTANCE_RESIZING = Constant('instance-resizing')
    INSTANCE_RESIZE_REJECTED = Constant('instance-resize-rejected')
    INSTANCE_RESIZE_CANCELLED = Constant('instance-resize-cancelled')
    INSTANCE_RESIZE_FAILED = Constant('instance-resize-failed')
    INSTANCE_RESIZED = Constant('instance-resized')
    INSTANCE_RESIZE_CONFIRM_BEGIN = Constant('instance-resize-confirm-begin')
    INSTANCE_RESIZE_CONFIRMING = Constant('instance-resize-confirming')
    INSTANCE_RESIZE_CONFIRM_REJECTED = Constant('instance-resize-confirm-rejected')
    INSTANCE_RESIZE_CONFIRM_CANCELLED = Constant('instance-resize-confirm-cancelled')
    INSTANCE_RESIZE_CONFIRM_FAILED = Constant('instance-resize-confirm-failed')
    INSTANCE_RESIZE_CONFIRMED = Constant('instance-resize-confirmed')
    INSTANCE_RESIZE_REVERT_BEGIN = Constant('instance-resize-revert-begin')
    INSTANCE_RESIZE_REVERTING = Constant('instance-resize-reverting')
    INSTANCE_RESIZE_REVERT_REJECTED = Constant('instance-resize-revert-rejected')
    INSTANCE_RESIZE_REVERT_CANCELLED = Constant('instance-resize-revert-cancelled')
    INSTANCE_RESIZE_REVERT_FAILED = Constant('instance-resize-revert-failed')
    INSTANCE_RESIZE_REVERTED = Constant('instance-resize-reverted')
    INSTANCE_GUEST_HEARTBEAT_ESTABLISHED = Constant('instance-guest-heartbeat-established')
    INSTANCE_GUEST_HEARTBEAT_DISCONNECTED = Constant('instance-guest-heartbeat-disconnected')
    INSTANCE_GUEST_HEARTBEAT_FAILED = Constant('instance-guest-heartbeat-failed')
    INSTANCE_GUEST_HEALTH_CHECK_FAILED = Constant('instance-guest-health_check-failed')
    SW_PATCH_AUTO_APPLY_START = Constant('sw-patch-auto-apply-started')
    SW_PATCH_AUTO_APPLY_INPROGRESS = Constant('sw-patch-auto-apply-inprogress')
    SW_PATCH_AUTO_APPLY_REJECTED = Constant('sw-patch-auto-apply-rejected')
    SW_PATCH_AUTO_APPLY_CANCELLED = Constant('sw-patch-auto-apply-cancelled')
    SW_PATCH_AUTO_APPLY_FAILED = Constant('sw-patch-auto-apply-failed')
    SW_PATCH_AUTO_APPLY_COMPLETED = Constant('sw-patch-auto-apply-completed')
    SW_PATCH_AUTO_APPLY_ABORT = Constant('sw-patch-auto-apply-abort')
    SW_PATCH_AUTO_APPLY_ABORTING = Constant('sw-patch-auto-apply-aborting')
    SW_PATCH_AUTO_APPLY_ABORT_REJECTED = Constant('sw-patch-auto-apply-abort-rejected')
    SW_PATCH_AUTO_APPLY_ABORT_FAILED = Constant('sw-patch-auto-apply-abort-failed')
    SW_PATCH_AUTO_APPLY_ABORTED = Constant('sw-patch-auto-apply-aborted')
    SW_UPGRADE_AUTO_APPLY_START = Constant('sw-upgrade-auto-apply-started')
    SW_UPGRADE_AUTO_APPLY_INPROGRESS = Constant('sw-upgrade-auto-apply-inprogress')
    SW_UPGRADE_AUTO_APPLY_REJECTED = Constant('sw-upgrade-auto-apply-rejected')
    SW_UPGRADE_AUTO_APPLY_CANCELLED = Constant('sw-upgrade-auto-apply-cancelled')
    SW_UPGRADE_AUTO_APPLY_FAILED = Constant('sw-upgrade-auto-apply-failed')
    SW_UPGRADE_AUTO_APPLY_COMPLETED = Constant('sw-upgrade-auto-apply-completed')
    SW_UPGRADE_AUTO_APPLY_ABORT = Constant('sw-upgrade-auto-apply-abort')
    SW_UPGRADE_AUTO_APPLY_ABORTING = Constant('sw-upgrade-auto-apply-aborting')
    SW_UPGRADE_AUTO_APPLY_ABORT_REJECTED = Constant('sw-upgrade-auto-apply-abort-rejected')
    SW_UPGRADE_AUTO_APPLY_ABORT_FAILED = Constant('sw-upgrade-auto-apply-abort-failed')
    SW_UPGRADE_AUTO_APPLY_ABORTED = Constant('sw-upgrade-auto-apply-aborted')


@six.add_metaclass(Singleton)
class _EventType(Constants):
    """
    Event Type Constants
    """
    UNKNOWN = Constant('unknown')
    STATE_EVENT = Constant('state-event')
    ACTION_EVENT = Constant('action-event')
    GUEST_HEARTBEAT_EVENT = Constant('guest-heartbeat-event')
    PROCESSING_ERROR = Constant('processing-error')


@six.add_metaclass(Singleton)
class _EventContext(Constants):
    """
    Event Context Constants
    """
    ADMIN = Constant('admin')
    TENANT = Constant('tenant')


@six.add_metaclass(Singleton)
class _EventImportance(Constants):
    """
    Event Importance Constants
    """
    UNKNOWN = Constant('unknown')
    HIGH = Constant('high')
    MEDIUM = Constant('medium')
    LOW = Constant('low')


@six.add_metaclass(Singleton)
class _EventInitiatedBy(Constants):
    """
    Initiated-By Constants
    """
    UNKNOWN = Constant('unknown')
    TENANT = Constant('tenant')
    INSTANCE = Constant('instance')
    INSTANCE_DIRECTOR = Constant('instance-director')


# Constant Instantiation
EVENT_ID = _EventId()
EVENT_TYPE = _EventType()
EVENT_CONTEXT = _EventContext()
EVENT_IMPORTANCE = _EventImportance()
EVENT_INITIATED_BY = _EventInitiatedBy()
