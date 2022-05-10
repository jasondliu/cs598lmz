import socket
# Test socket.if_indextoname()
import subprocess
# Test subprocess.Popen()
import sys
# Test sys.platform
import time
# Test time.sleep()

import pytest

from tests.common import (
    assert_python_ok,
    run,
    skip_if_no_network,
    skip_unless_netifaces_imported,
    skip_unless_platform,
)

# Skip tests if IPv6 is not supported by the system
skip_unless_platform('linux', 'freebsd', 'openbsd', 'netbsd', 'darwin',
                     'sunos5')

# Skip tests if the netifaces module is not available
skip_unless_netifaces_imported()

# Skip tests if the system has no network interface
skip_if_no_network()


