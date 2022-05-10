import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys

__version__ = '0.5.2'

# The libnotify library
libnotify = ctypes.CDLL(ctypes.util.find_library('notify'))

# The libnotify API
class NotifyNotification(ctypes.Structure):
    """
    A libnotify notification.

    :ivar _title: The title of the notification.
    :ivar _body: The body of the notification.
    :ivar _icon: The icon of the notification.
    :ivar _timeout: The timeout of the notification.
    :ivar _urgency: The urgency of the notification.
    """

    _fields_ = [('_title', ctypes.c_char_p),
                ('_body', ctypes.c_char_p),
                ('_icon', ctypes.c_char_p),
                ('_timeout', ctypes.c_int),
                ('_urgency', ctypes.c_int)]

    def __init__(self, title, body, icon, timeout, urgency
