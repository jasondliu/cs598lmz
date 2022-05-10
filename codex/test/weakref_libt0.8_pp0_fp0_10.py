import weakref
from collections import namedtuple

from splunk.util import normalizeBoolean as nb

from splunk.models.base import SplunkAppObjModel
from splunk.models.field import Field, BoolField
from splunk.models.convenience import remove_default_fields

from splunktalib.common import log
import splunktalib.conf_manager.ta_conf_manager as tcm
import splunktalib.file_monitor as fm


_LOGGER = log.Logs().get_logger("util")


def reload_apps(body):
    reload_via_confmgr(body)
    # TODO: reload via rest
    return True


def reload_via_confmgr(body):
    conf_name = "app_conf"
    stanza = body.get('name')
    manager = tcm.TAConfManager(conf_name, _LOGGER)
    fields = {'disabled': 'false'}
    if body.get('disabled', ''):
        fields['disabled'] = 'true'
