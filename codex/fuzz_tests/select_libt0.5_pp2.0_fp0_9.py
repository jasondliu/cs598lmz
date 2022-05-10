import select
import subprocess
import sys
import time

import pytest

from . import helpers

# The tests in this module are designed to be run once per test session.
# The tests in this module should be run *before* other tests that use
# the server.
#
# The tests in this module are designed to be run on the local machine,
# not the server.
#
# The tests in this module are designed to run with a server that is
# running on the local machine.
#
# The tests in this module are designed to run with a server that is
# running on the default port.
#
# The tests in this module are designed to run with a server that is
# running with the default server key.

@pytest.fixture(scope='session')
def server_process():
    # Start the server as a subprocess.
    # Wait for the server to start accepting connections.
    # Return the subprocess.
    args = [sys.executable, '-m', 'tlsdump.tlsdump', '--no-tls-verify']
    server_process = sub
