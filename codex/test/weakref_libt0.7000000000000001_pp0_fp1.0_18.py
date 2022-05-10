import weakref

from . import __version__
from . import get_settings
from . import get_version
from . import logger
from . import signal
from . import utils


class _UIApplication(object):
    """
    A class that mimics the behavior of UIApplication to support running
    a Pythonista keyboard extension.
    """

    def __init__(self):
        self._main_window = None
        self._delegate = None
        self._proxy_delegate = None
        self._active_touches = {}
        self._settings_changed_token = None
        self.keyboard_active = True
        self.keyboard_frame_end = None
        self.keyboard_frame_begin = None
        self.keyboard_frame = None
        self.autorotate = True
        self.status_bar_hidden = True
        self.status_bar_orientation = 0
        self.status_bar_frame = None
        self.status_bar_height = 0
        self.application_supports_shaking_to_edit = False
