import select
import threading

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.translation import ugettext as _

from audit_log.models.managers import LogEntryManager
from audit_log.models.fields import LastUserField

from tendenci.apps.site_settings.utils import get_setting
from tendenci.apps.user_groups.models import Group
from tendenci.apps.user_groups.utils import get_default_group
from tendenci.apps.user_groups.utils import get_group_by_name
from tendenci.apps.user_groups.utils import get_group_by_pk
from tendenci.apps.perms.utils import (get_notice_recipients,
                                       get_object_name,
                                       has_perm)
from tendenci.apps.perms.utils import (update_perms_and_save,
                                       set_groups_perms,
                                       get_query_filters,
                
