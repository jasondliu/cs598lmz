import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(_core.Object):
    def __init__(self, app_id=None, app_name=None, app_version=None,
                 app_url=None, app_description=None, app_copyright=None,
                 app_license=None, app_license_url=None, app_icon=None,
                 app_website=None, app_website_label=None,
                 app_bugs_url=None, app_create_desktop_entry=True,
                 app_no_window=False, app_startup_id=None,
                 app_menu=None, app_dock=None, app_accels=None,
                 app_resource_base_path=None, app_resource_suffix=None,
                 app_flags=0):
        super().__init__()
        self._app_id = app_id
        self._app_name = app_name
        self._app_version = app_version
