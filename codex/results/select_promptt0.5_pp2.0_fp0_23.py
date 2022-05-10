import select
# Test select.select
import select
import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.bind(("", 50000))
s.listen(5)

inputs = [s, sys.stdin]
outputs = []

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for r in readable:
        if r is s:
            connection, addr = r.accept()
            connection.setblocking(0)
            inputs.append(connection)
        elif r is sys.stdin:
            junk = sys.stdin.readline()
            break
        else:
            data = r.recv(1024)
            if data:
                print("received:", data)
                outputs.append(r)
            else:
                inputs.remove(r)
    for w in writable:
        w.send("echo: " + data)
        outputs.remove(w)
    for e in exceptional:
