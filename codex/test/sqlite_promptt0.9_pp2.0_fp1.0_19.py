import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('lists.db')

from .utils import log


def get_module_path():
    return os.path.dirname(os.path.abspath(__file__))


def get_plugin_rpc_client():
    plugin_rpc_client = _PluginClient()
    try:
        return plugin_rpc_client.client
    except RuntimeError:
        return None


def run_in_thread(target):
    def new_target(*args, **kwargs):
        t = threading.Thread(target=target, args=args, kwargs=kwargs)
        t.start()

    return new_target


class CancellationToken:
    def __init__(self):
        self._was_cancelled = False

    def is_cancelled(self):
        return self._was_cancelled

    def cancel(self):
        self._was_cancelled = True

    def reset(self):
        self._was_cancelled = False


