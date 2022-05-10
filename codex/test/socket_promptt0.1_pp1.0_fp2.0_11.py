import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import socket
import array
import struct
import select
import time
import platform
import subprocess
import re

from test import support
from test.support import import_module

# Skip test if there is no if_indextoname()
support.get_attribute(socket, 'if_indextoname')

# Skip test if there is no if_nametoindex()
support.get_attribute(socket, 'if_nametoindex')

# Skip test if there is no if_nameindex()
support.get_attribute(socket, 'if_nameindex')

# Skip test if there is no if_nametoindex()
support.get_attribute(socket, 'if_nametoindex')

# Skip test if there is no if_nameindex()
support.get_attribute(socket, 'if_nameindex')

# Skip test if there is no SIOCGIFADDR ioctl
support.get_attribute(socket, 'SIOCGIFADDR')

# Skip test if there is no SIOC
