import socket
# Test socket.if_indextoname()
#
# Copyright (C) 2005 Michael Richardson <mcr@xelerance.com>
# Copyright (C) 2010-2012 Paul Wouters <paul@xelerance.com>
# Copyright (C) 2012 Avesh Agarwal <avagarwa@redhat.com>
# Copyright (C) 2012 Paul Wouters <pwouters@redhat.com>
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
#

import os
import sys
import pexpect
import time
from util
