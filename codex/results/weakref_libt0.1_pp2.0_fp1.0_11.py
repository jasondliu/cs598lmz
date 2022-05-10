import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(object):
    """
    The application object.
    """

    def __init__(self, app_name, app_version):
        self._app_name = app_name
        self._app_version = app_version
        self._windows = []
        self._windows_by_id = {}
        self._windows_by_handle = {}
        self._windows_by_name = {}
        self._windows_by_title = {}
        self._windows_by_class = {}
        self._windows_by_class_name = {}
        self._windows_by_class_name_re = {}
        self._windows_by_process = {}
        self._windows_by_process_name = {}
        self._windows_by_process_name_re = {}
        self._windows_by_control_id = {}
        self._windows_by_control_id_re = {}
        self._windows_by_visible = {}
        self
