import select
import socket
import sys
import time
import traceback

import pytest

import trio
from trio import socket as tsocket
from trio.testing import open_stream_to_socket_listener, open_stream_to_socket_connected


def test_socket_stream_basic():
    # Create a socket and bind it to a local port
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    sock.listen(1)
    host, port = sock.getsockname()

    # Open a stream to that socket
    async def client():
        stream = await trio.open_tcp_stream(host, port)
        await stream.send_all(b"hello")
        await stream.aclose()

    async def server():
        client_sock, _ = await trio.to_thread.run_sync(sock.accept)
        stream = trio.SocketStream(client_sock)
        assert await stream.receive_some(5) == b"hello"
        await stream.aclose()

    with trio
