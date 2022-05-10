import socket
import sys

TARGET = ("www.xknx.org", 80)

message = b"""GET / HTTP/1.1\r
Host: www.xknx.org\r
Connection: Upgrade\r
Upgrade: websocket\r
Sec-WebSocket-Version: 13\r
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==\r
Sec-WebSocket-Protocol: xknx\r
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits\r
\r
"""


def main() -> None:
    """Main method."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(TARGET)
        sock.sendall(message)
        received = str(sock.recv(1024), "utf-8")
    print(received)


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except
