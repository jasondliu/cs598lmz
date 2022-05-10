import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import socket

from test.support import (
    TESTFN, run_unittest, find_unused_port, requires_mac_ver,
    requires_linux_version, requires_linux_version_or_kernel,
    requires_linux_version_or_kernel_or_android,
    requires_android_version, requires_freebsd_version,
    requires_netbsd_version, requires_unix_version,
    requires_unix_version_or_kernel, requires_unix_version_or_kernel_or_android,
    requires_android_emulator,
    )

if sys.platform == 'darwin':
    from test.support import import_module
    import_module('SystemConfiguration')

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import termios
except ImportError:
    termios = None

try:
    import resource
except ImportError:
    resource = None

