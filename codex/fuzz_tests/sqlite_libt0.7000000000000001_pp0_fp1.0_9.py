import ctypes
import ctypes.util
import threading
import sqlite3
import os

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from yubihsm import YubiHsm, YubiHsmError
from yubihsm.objects import AuthKey, HmacKey, AsymmetricKey
from yubihsm.defs import ALGORITHM, CAPABILITY

from yubiadmin import __version__
from yubiadmin.yubikey import YubiKey
from yubiadmin.yubico_piv_tool import YkPivTool
from yubiadmin.yubihsm_connector import YubiHsmConnectorClient
from yubiadmin.card_widget import CardWidget
from yubiadmin.yubihsm_client import YubiHsmClient
from yubiadmin.gtk_plugin import GtkPlugin


LIBUSB = None

try:
    import usb.core
except ImportError:
    pass
else:
    LIBUSB = True


class YubiAdmin:
    """
    This class represents the main interface for the application.

