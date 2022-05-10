import select
import socket
import sys
import threading
import time
from collections import deque

import pytest
from _pytest.monkeypatch import MonkeyPatch
from pytest_mock import MockFixture

from pytest_socket import SocketError, SocketTimeout
from pytest_socket.plugin import (
    _SocketConnection,
    _SocketServer,
    _SocketServerThread,
    _SocketWrapper,
    _accept_connection,
    _get_socket_connection,
    _get_socket_server,
    _get_socket_wrapper,
    _get_socket_wrapper_from_server,
    _get_socket_wrapper_from_socket,
    _get_socket_wrapper_from_thread,
    _is_socket_server,
    _is_socket_server_thread,
    _is_socket_wrapper,
    _is_socket_wrapper_from_server,
    _is_socket_wrapper_from_socket,
    _is_socket_wrapper_from_thread,
    _is_valid_socket_server,
    _is_valid_socket
