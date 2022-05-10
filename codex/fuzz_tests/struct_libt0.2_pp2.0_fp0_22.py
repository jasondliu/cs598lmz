import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# These modules are not built-in, but we want to make them available
# in the micropython namespace.
import array
import collections
import fcntl
import framebuf
import io
import json
import math
import os
import select
import socket
import struct
import sys
import termios
import time
import uerrno
import uhashlib
import uio
import ujson
import uos
import upip
import upip_utarfile
import ure
import uselect
import usocket
import ussl
import ustruct
import utime
import uzlib
import zlib

# These modules are not built-in, but we want to make them available
# in the micropython namespace, and they are implemented in C.
import ubinascii
import ucollections
import ucryptolib
import uerrno
import uhashlib
import uheapq
import uio
import ujson
import uos
import
