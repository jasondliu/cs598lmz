import socket
# Test socket.if_indextoname()
#
# This test needs to run as root, otherwise it'll fail.
#
# This test is not included in the default test suite, since it needs to run
# as root.
#
# This test is also not included in the default test suite, since it
# requires the 'iproute' tool to be installed.
#
# This test is also not included in the default test suite, since it
# requires the 'ip' tool to be installed.
#
# This test is also not included in the default test suite, since it
# requires the 'brctl' tool to be installed.
#
# This test is also not included in the default test suite, since it
# requires the 'bridge' tool to be installed.
#
# This test is also not included in the default test suite, since it
# requires the 'ethtool' tool to be installed.
#
# This test is also not included in the default test suite, since it
# requires the 'ip' tool to be installed.

import os
import socket
import sys
import time
import unittest

from test import support


