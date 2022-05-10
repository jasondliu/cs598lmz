import socket
# Test socket.if_indextoname()
# (see also test_ifnameindex, which tests socket.if_nameindex())
import sys

if sys.platform.startswith('freebsd'):
    # The code below has been tested on FreeBSD 8.0, 8.1 and 9.0-CURRENT
    # with a loopback interface only.
    raise unittest.SkipTest('test skipped on FreeBSD')

if sys.platform.startswith('linux'):
    # The code below has been tested on Linux 2.6.32-5-686 #1 SMP
    # with a loopback interface only.
    raise unittest.SkipTest('test skipped on Linux')

if sys.platform.startswith('netbsd'):
    # The code below has been tested on NetBSD 5.1 with a loopback
    # interface only.
    raise unittest.SkipTest('test skipped on NetBSD')

if sys.platform.startswith('openbsd'):
    # The code below has been tested on OpenBSD 4.6 with a loopback
    # interface only.
    raise un
