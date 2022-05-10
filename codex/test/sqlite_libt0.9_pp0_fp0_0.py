import ctypes
import ctypes.util
import threading
import sqlite3
import functools
import select

db = sqlite3.connect("tb_keys.db")


class DeviceOpen(threading.Thread):
    def __init__(self, device_path, callback=None, *args, **kwargs):
        self.__dict__.update(locals())
        del self.self
        self.__dev = None
        self.__event = threading.Event()
        super(DeviceOpen, self).__init__(*args, **kwargs)

    def run(self):
        self.__dev = open(self.device_path)
        self.__event.set()
        while self.is_alive():
            ret = select.select([self.__dev], [], [], 1)
            if not self.is_alive():
                break
            if len(ret[0]) == 1:
                callback = functools.partial(
                    self.callback,
                    device_path=self.device_path
                    )
                self._Thread__stop()
                callback()

