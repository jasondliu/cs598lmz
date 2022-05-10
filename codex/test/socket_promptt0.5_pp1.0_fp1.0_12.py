import socket
# Test socket.if_indextoname
#
# Copyright (C) 2016 Andrew Cagney
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.  See <http://www.fsf.org/copyleft/gpl.txt>.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

import os
import sys
import unittest

from fab import testutil
from fab import if_indextoname

from fab import logutil

from fab import skip
skip.unless(sys.platform.startswith("linux"), "requires Linux")
skip.unless(os.path.exists("/proc/net/if_inet6"), "requires /proc/net/if_inet6")

