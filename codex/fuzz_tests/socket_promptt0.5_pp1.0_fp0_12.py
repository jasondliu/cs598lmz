import socket
# Test socket.if_indextoname()
#
# This test checks that socket.if_indextoname()
# returns the correct name for the given index.
#
# Author: Werner Fink <werner@suse.de>, 2007
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version
# 2 of the License, or (at your option) any later version.

import os
import sys
import socket
import struct
import fcntl
import unittest

def if_indextoname(index):
    ifindex = struct.pack('i', index)
    return fcntl.ioctl(sock.fileno(), 0x8933, ifindex)[:16].strip('\0')

class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        self.assertEqual(socket.if_indextoname(1), if_indextoname(1))
        self.assertE
