import select
import socket
import sys
import struct
import time

import docker
import pytest

from docker_registry_client_async import client, constants, errors


@pytest.fixture
def client_v2():
    return client.AsyncClient("localhost:5000", "v2")


@pytest.fixture
def client_v1():
    return client.AsyncClient("localhost:5000", "v1")


@pytest.fixture
def client_v1_ssl():
    return client.AsyncClient("localhost:5001", "v1", ssl_verify=False)


@pytest.fixture
def client_v2_ssl():
    return client.AsyncClient("localhost:5001", "v2", ssl_verify=False)


def wait_for_connection(host, port, timeout=60):
    start = time.time()
    while True:
        try:
            s = socket.create_connection((host, port), timeout=timeout)
            s.close()
            break
        except socket.error as e:

