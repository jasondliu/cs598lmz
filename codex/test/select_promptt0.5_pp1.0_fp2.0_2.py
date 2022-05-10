import select
# Test select.select

# create a non-blocking socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)

# connect to a local server
s.connect(('www.google.com', 80))

# wait until the connection is complete
while True:
    try:
        s.send(b'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n')
        break
    except BlockingIOError:
        pass

# wait until the data is received
while True:
    try:
        data = s.recv(4096)
    except BlockingIOError:
        continue
    else:
        print(data.decode('utf-8'))
        break

# close the connection
s.close()
# select.select()

# create a non-blocking socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)

# connect to a local server
