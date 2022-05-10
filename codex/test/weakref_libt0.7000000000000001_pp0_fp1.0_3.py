import weakref
from infi.systray.base_tray import BaseTray
from infi.systray import systray_service
from infi.systray.errors import UnsupportedPlatformError

logger = logging.getLogger(__name__)


class WindowsTray(BaseTray):
    def __init__(self):
        super().__init__()
        self._tray_icon_name = 'main_icon'
        self._ref_obj = weakref.ref(self)
        self._id_counter = 0
        self._hwnd = None

