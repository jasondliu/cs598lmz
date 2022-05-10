import select
import sys
import time

import pytest

from tests.common import exec_command, get_free_port, get_unused_port_like
from tests.common import kill_process
from tests.common import wait_for_port_to_disappear
from tests.common import wait_for_port_to_appear

from . import (
    get_process_output,
    get_process_output_and_error,
    get_process_output_lines,
    get_process_output_lines_and_error,
    get_process_output_until_output,
    get_process_output_until_output_and_error,
    get_process_output_until_timeout,
    get_process_output_until_timeout_and_error,
)

# The port used by the server.
PORT = get_free_port()

# The port used by the client.
CLIENT_PORT = get_free_port()


@pytest.fixture(scope="module")
def server_process(request):
    """
    Fixture
