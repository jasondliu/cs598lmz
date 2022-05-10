import select
import subprocess
import sys
import time

from definitions import (
    CLIENT_NAME,
    DEFAULT_TIMEOUT,
    MAX_PACKET_SIZE,
    MAX_TIMEOUT,
    MIN_TIMEOUT,
    SERVER_NAME,
    TIMEOUT_INCREMENT,
    TIMEOUT_THRESHOLD,
    TIMEOUT_TRIES,
)
from packet import Packet
from utils import (
    bytes_to_int,
    get_checksum,
    int_to_bytes,
    send_and_receive,
    send_packet,
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 client.py <port>", file=sys.stderr)
        sys.exit(1)

    port = int(sys.argv[1])
