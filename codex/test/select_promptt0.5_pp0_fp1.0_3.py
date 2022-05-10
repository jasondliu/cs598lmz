import select
# Test select.select()

import socket
import time
import select


def test_select():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 5000))
    s.listen(10)

    while True:
        inputready, outputready, exceptready = select.select([s], [], [])
