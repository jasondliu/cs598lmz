import socket

# Address
HOST = ''
PORT = 8001
ADDR = (HOST,PORT)
BUFSIZE = 4096

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

print 'listening ...'

# Main loop
while True:
    try:
        conn, addr = s.accept()
        print '... connected!'
        data = conn.recv(BUFSIZE)
        if not data:
            print 'no data'
            break
        print data
        conn.send(data)
        conn.close()
        print 'closed connection'
    except KeyboardInterrupt:
        s.close()
        print 'shutting down ...'
        break
