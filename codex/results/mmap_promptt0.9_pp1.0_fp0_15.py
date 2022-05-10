import mmap
# Test mmap.mmap and mmap.ACCESS_READ
from mmap import *
from mmap import mmap, ACCESS_READ
print mmap
print ACCESS_READ

#from threadext import *
from threadext import *
from threadext import start_new_thread as _start_new_thread
_start_new_thread('foobar', 'abc123')

from httplib import *
from httplib import HTTPConnection
from httplib import HTTP
import httplib
from httplib import HTTPConnection
print HTTPConnection
import httplib
print httplib.HTTPConnection

from thread import *
from thread import start_new_thread as _start_new_thread
_start_new_thread('foobar', 'abc123')

from rfc822 import *
from rfc822 import Message
from rfc822 import AddressList
from rfc822 import AddrlistClass
from rfc822 import AddressList
print Message
print AddressList
print AddrlistClass
print AddressList

from Cookie import *
from Cookie import SimpleCookie

