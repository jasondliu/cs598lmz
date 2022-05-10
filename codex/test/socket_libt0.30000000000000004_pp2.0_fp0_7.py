import socket
import sys
import threading
import time

import pytest

from pytest_localserver.http import WSGIServer


@pytest.fixture
def server():
    return WSGIServer()


def test_server_start_stop(server):
    server.start()
    assert server.is_running()
    server.stop()
    assert not server.is_running()


def test_server_start_stop_start(server):
    server.start()
    assert server.is_running()
    server.stop()
    assert not server.is_running()
    server.start()
    assert server.is_running()
    server.stop()
    assert not server.is_running()


def test_server_start_stop_start_stop(server):
    server.start()
    assert server.is_running()
    server.stop()
    assert not server.is_running()
    server.start()
    assert server.is_running()
    server.stop()
    assert not server.is_running()
