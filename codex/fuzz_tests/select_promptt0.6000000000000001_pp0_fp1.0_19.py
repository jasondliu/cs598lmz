import select
# Test select.select
import socket
import time

port = 50007
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

input = [sock]
running = 1
while running:
    inputready, outputready, exceptready = select.select(input, [], [])

    for s in inputready:
        if s == sock:
            client, address = sock.accept()
            input.append(client)
        else:
            data = s.recv(1024)
            if data:
                print "Data:", data
                print "Address:", s.getpeername()
                s.send(data)
            else:
                s.close()
                input.remove(s)

sock.close()
