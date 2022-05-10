import select
import socket
import sys
import time

from crypto_util import crypto_util
from message_pb2 import Message

BUFSIZ = 4096

def main():
    if len(sys.argv) != 4:
        sys.exit('Usage: %s <host> <port> <key>"' % sys.argv[0])

    host = sys.argv[1]
    port = int(sys.argv[2])

    cryptoUtil = crypto_util()

    try:
        key = cryptoUtil.getKey(sys.argv[3])
    except ValueError:
        sys.exit("invalid key")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        if s is None:
            sys.exit('cannot open socket')

        message = Message()
        message.sender = "client"
        message.request = "hello"
        message.timestamp = int(time.time())

        messageBytes = cryptoUtil.serializeMessage
