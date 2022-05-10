import lzma
lzma.LZMAError

import os
os.EX_OK

import posix
posix.EX_OK

import pwd
pwd.struct_passwd

import select
select.select

import signal
signal.SIGALRM

import socket
socket.AF_INET6

import stat
stat.S_ISLNK

import sys
sys.version_info

import termios
termios.tcgetattr

import time
time.tzname

import tty
tty.setraw

import unicodedata
unicodedata.normalize

import zlib
zlib.compress

# These modules are not available on all platforms
try:
    import grp
    grp.struct_group
except ImportError:
    pass

try:
    import nis
    nis.match
except ImportError:
    pass

try:
    import readline
    readline.get_history_length
except ImportError:
    pass

