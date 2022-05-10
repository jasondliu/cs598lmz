import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if os.name != 'nt':
    print('Test only supported on Windows')
    sys.exit(0)

if_indextoname = socket.if_indextoname

def test_if_indextoname():
    # Test if_indextoname()
    if_indextoname(1)
    if_indextoname(2)
    if_indextoname(3)
    if_indextoname(4)
    if_indextoname(5)
    if_indextoname(6)
    if_indextoname(7)
    if_indextoname(8)
    if_indextoname(9)
    if_indextoname(10)
    if_indextoname(11)
    if_indextoname(12)
    if_indextoname(13)
    if_indextoname(14)
    if_indextoname(15)
    if_indextoname(16)
