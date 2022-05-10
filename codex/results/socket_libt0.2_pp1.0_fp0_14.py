import socket
import sys
import time

import pytest

from . import utils


@pytest.fixture
def server_address():
    return ('127.0.0.1', 0)


@pytest.fixture
def server(server_address):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(server_address)
    server.listen(1)
    yield server
    server.close()


@pytest.fixture
def client(server_address):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)
    yield client
    client.close()


@pytest.fixture
def server_client(server, client):
    yield server, client


def test_server_client(server_client):
    server, client = server_client
    server_conn, _ =
