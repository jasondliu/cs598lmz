import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import hashlib
import socket
import pwd
import struct
import platform
import string
import errno
import logging

# GLib2
from gi.repository import GLib
from gi.repository import GObject

# Telepathy
import telepathy

# Salut
from gabbletest import make_result_iq, make_presence, make_disco_reply
from gabbletest import exec_test
from servicetest import (
    make_channel_proxy, wrap_channel, assertEquals, assertContains
    )
import constants as cs
import ns

if os.name == 'nt':
    from win32file import FILE_BEGIN
    from win32file import FILE_END
    from win32event import INFINITE
else:
    import fcntl

class DataFormsTest(object):
    """
    A base class to test data forms.

    This class is responsible for creating a stream, connect to Gabble,
    create a muc channel and request the data forms on the muc channel.
