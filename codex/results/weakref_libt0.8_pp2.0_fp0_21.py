import weakref

from cefpython3 import cefpython as cef

# Global `App()` instance
# WARNING: You must initialize `App()` before calling `Cef()`
# and you must do it only once.
_g_app = None

class Cef:
    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------

    def __init__(self, logger):
        # `_g_app` is global, it must be set only once,
        # otherwhise it will throw an exception.
        global _g_app
        if _g_app is not None:
            raise RuntimeError("`App()` was already initialized elsewhere")
        # Create global `App()` instance
        _g_app = App(logger)

    def run(self, main_url=None, startup_urls=None):
        if main_url is not None:
            _g_app.set_main_url(main_url)
        if startup_urls is not None:
            _g_app.set_startup_urls(startup_urls)
