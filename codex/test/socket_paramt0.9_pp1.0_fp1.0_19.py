import socket
socket.if_indextoname(socket.if_nametoindex("etho"))

import os

username = os.environ["USERNAME"]
print(username)
os.environ["TEST"] = "foobar"

from ctypes import *
from ctypes.util import find_library
libc = CDLL(find_library("c"))

from gi.repository import Gtk

print(gi.require_version("Gtk", "3.0"))

from gi.repository import Notify

from datetime import datetime, timezone
print(datetime.now(timezone.utc).astimezone())
