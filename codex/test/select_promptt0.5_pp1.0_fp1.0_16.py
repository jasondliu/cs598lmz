import select
# Test select.select
# test_select.py

import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8001))
sock.listen(5)

inputs = [sock]
outputs = []

while True:
    rs, ws, es = select.select(inputs, outputs, inputs)
