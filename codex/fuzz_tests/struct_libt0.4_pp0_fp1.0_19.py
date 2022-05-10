import _struct
import _thread
import _threading
import _time
import _warnings
import _weakref
import _weakrefset
import _winapi
import _winreg

import os
import sys

# This is the same as sys.stdin, but it is guaranteed to be open
# in text mode.
_stdin = open(sys.stdin.fileno(), 'r', encoding=sys.stdin.encoding,
              closefd=False)

# This is the same as sys.stdout, but it is guaranteed to be open
# in text mode.
_stdout = open(sys.stdout.fileno(), 'w', encoding=sys.stdout.encoding,
               closefd=False)

# This is the same as sys.stderr, but it is guaranteed to be open
# in text mode.
_stderr = open(sys.stderr.fileno(), 'w', encoding=sys.stderr.encoding,
               closefd=False)

# This is the same as sys.stdin, but it is guaranteed to be open
#
