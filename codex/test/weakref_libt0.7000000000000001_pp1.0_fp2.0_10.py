import weakref

from . import proxy
from . import control
from . import settings

from .utils.log import Log
from .utils import util

from .control.type_converters import to_ctypes, to_py
from .control.typing import Action, ActionFlag, ActionPriority, ActionSignature, EventSignature, Event
from .control.type_converters import to_ctypes


class ActionContext(object):
    def __init__(self, action, instance, event, control, settings_handler, user_data, data_context, log_handler=None, log_helper=None):
        self._action = action
        self._instance = instance
        self._event = event
        self._control = control
        self._settings_handler = settings_handler
        self._user_data = user_data
        self._data_context = data_context
        self._log_handler = log_handler
        self._log_helper = log_helper

    def params(self):
        return self._action.params

