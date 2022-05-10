import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import json
import sys
import contextlib

from . import _libsmbclient

class SMBError(Exception):
    pass

class SMBTimeoutError(SMBError):
    pass

class SMBProtocolError(SMBError):
    pass

class SMBProtocolUnsupported(SMBProtocolError):
    pass

class SMBAuthenticationError(SMBError):
    pass

class SMBAuthenticationDenied(SMBAuthenticationError):
    pass

class SMBAuthenticationBadUsernamePassword(SMBAuthenticationError):
    pass

class SMBAuthenticationBadChallenge(SMBAuthenticationError):
    pass

class SMBNoSuchFile(SMBError):
    pass

class SMBInvalidPath(SMBError):
    pass

class SMBFileExists(SMBError):
    pass

class SMBFileNotFound(SMBError):
    pass

class SMBFileNotADirectory(SMBError):
    pass

class
