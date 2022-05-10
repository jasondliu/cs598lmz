import weakref
import os

import ptah
from ptah.action_settings import ID_ACTION_INFOS
from ptah.view import View, register_view

from cgi import escape
import simplejson

factory = ptah.get_cfg_storage('ptah:form:factory')

cfgtool = getattr(ptah.auth_service, 'cfg')
auth_cfg = cfgtool.get('ptah:form:authentication', None)


class ActionSubscriber(object):
    """subscriber for local actions"""

    def __init__(self, discriminator):
        self.discriminator = discriminator

    def __call__(self, context, request, info):
        action = info['action']
        route_name = info.get('route', 'plocals')

        settings = action.app_settings.get(route_name)
        if settings is not None:
            info = settings.get(self.discriminator)
