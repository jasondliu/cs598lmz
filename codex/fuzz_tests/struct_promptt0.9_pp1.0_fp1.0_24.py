import _struct
# Test _struct.Struct
'd:df:df:d' % (1, 3.4, 5.4, 7.4)

try:
    d = 5.4
except Exception as e:
    print(e)

try:
    d = bytes(5.4)
except Exception as e:
    print(e)

try:
    d = 5.4 + b''
except Exception as e:
    print(e)

from _compat import *
from uPython import *
from usocket import *
from ulogging import *
from utime import *
from network import *
from uselect import *
from urequests import *
