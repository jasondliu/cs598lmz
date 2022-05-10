import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import json
import base64
import os
import platform

from socketserver import ThreadingTCPServer
from socketserver import BaseRequestHandler

from lib.common.defines import KERNEL32
from lib.common.defines import WM_CLOSE
from lib.common.defines import WM_QUERYENDSESSION
from lib.common.defines import ENDSESSION_CLOSEAPP
from lib.common.defines import WTS_SESSION_LOCK
from lib.common.defines import WTS_SESSION_UNLOCK
from lib.common.defines import WTS_CONSOLE_CONNECT
from lib.common.defines import WTS_CONSOLE_DISCONNECT
from lib.common.defines import WTS_REMOTE_CONNECT
from lib.common.defines import WTS_REMOTE_DISCONNECT
from lib.common.defines import WTS_SESSION_LOGON
from lib.common.defines import WTS_SESSION_LOGOFF
from lib.common.defines import WTS_SESSION_REMOTE_CONTROL

from
