import bz2
bz2.BZ2Compressor().compress(b'Hellodasdas')

# this example shows how to hook the lower-level bz2 library
import socket
import time
import bz2
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',10000))
compressor = bz2.BZ2Compressor()
sock.sendall(compressor.compress(b'bi\n'))
sock.sendall(compressor.compress(b'i love you!\n'))
time.sleep(2)
sock.sendall(compressor.compress(b'pray for me'))
sock.sendall(compressor.flush())

inputs = [sock]
outputs = []
message_queues = {}
while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
        data = s.recv(1024)
        if data:
            print('Received
