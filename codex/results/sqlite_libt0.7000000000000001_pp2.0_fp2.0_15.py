import ctypes
import ctypes.util
import threading
import sqlite3
import os

if os.name == "nt":
    lib = ctypes.windll.LoadLibrary("lib/c/win32/libnotify-native.dll")
else:
    lib = ctypes.CDLL(ctypes.util.find_library("notify-native"))

lib.notify_init("dzen-notify")

class Notification(object):
    """A notification object represents a libnotify notification,
    but with a few custom attributes.

    """
    def __init__(self, title, summary, body, icon = None):
        self._title = title
        self._summary = summary
        self._body = body
        self._icon = icon

        self._notification = lib.notify_notification_new(
            title, summary, icon, None)

    def show(self):
        """Show the notification.

        """
        lib.notify_notification_show(self._notification, None)

    def hide(self):
        """Hide the notification.

        """
        lib.notify_notification_close(self
