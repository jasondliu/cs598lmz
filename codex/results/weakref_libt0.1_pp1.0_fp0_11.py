import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(object):
    def __init__(self, app):
        self._app = app
        self._windows = []

    def run(self):
        self._app.run()

    def quit(self):
        self._app.quit()

    def add_window(self, window):
        self._windows.append(window)

    def remove_window(self, window):
        self._windows.remove(window)

    def get_windows(self):
        return self._windows

    def get_window(self, index):
        return self._windows[index]

    def get_window_count(self):
        return len(self._windows)

    def get_name(self):
        return self._app.get_name()

    def get_display_name(self):
        return self._app.get_display_name()

    def get_bundle_id(self):
        return self._app.get_bundle_id()
