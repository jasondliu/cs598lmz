import socket
import subprocess
import threading
import time

import docker
import pytest

from .common import TEST_IMAGE, get_open_port, get_random_str
from .conftest import (
    wait_until_exists,
    wait_until_not_exists,
    wait_until_running,
    wait_until_stopped,
)

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


@pytest.mark.skipif(
    not pytest.config.getoption("--runslow"), reason="need --runslow option to run"
)
@pytest.mark.timeout(30)
@pytest.mark.skip(reason="We no longer test the Docker API server.")
def test_container_get_container_api_version(client):
    assert client.version()["ApiVersion"]


