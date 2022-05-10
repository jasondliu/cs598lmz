import ctypes
import ctypes.util
import threading
import sqlite3

import constants
import utils

class UnsupportedPlatform(Exception):
    pass

class DBusNotFound(Exception):
    pass

class DBusError(Exception):
    pass

class DBusNotConnectedError(DBusError):
    pass

class DBusNotImplementedError(DBusError):
    pass

class DBusNotSupportedError(DBusError):
    pass

class DBusNotAvailableError(DBusError):
    pass

class DBusNotAuthorizedError(DBusError):
    pass

class DBusTimeoutError(DBusError):
    pass

class DBusNoReplyError(DBusError):
    pass

class DBusNameHasNoOwnerError(DBusError):
    pass

class DBusInvalidArgsError(DBusError):
    pass

class DBusUnknownMethodError(DBusError):
    pass

class DBusUnknownObjectError(DBusError):
    pass

class DBusUnknownInterfaceError(DBusError):
    pass

