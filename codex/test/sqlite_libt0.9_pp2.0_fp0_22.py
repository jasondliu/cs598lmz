import ctypes
import ctypes.util
import threading
import sqlite3
import struct
import errno
if sys.version_info < (3,):
  import ConfigParser as configparser
else:
  import configparser
  long = int

class DeviceNotFoundException(Exception):
  pass

class ConnectionFailure(Exception):
  pass

class BTLEException(Exception):
  pass

class BTLEDisconnectError(BTLEException):
  pass

class NotificationTimeout(BTLEException):
  pass

class NotificationError(BTLEException):
  pass

class _BLEDescriptor:
  def __init__(self, handle, uuid, properties):
    self.handle = handle
    self.uuid = uuid
    if len(self.uuid) == 2:
      self.uuid = BASE_UUID + self.uuid
    elif len(self.uuid) != 16:
      raise BTLEException("UUID not valid length")
    self.properties = properties

