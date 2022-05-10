import select
# Test select.select
import socket

#listen to connections on port 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(5)

#listen for incoming data on the socket
def listen(sock):
    data = sock.recv(1024)
    if data:
        print(data)

#accept any new connections
def accept(sock):
    conn, addr = sock.accept()
    print('Connected by', addr)
    return conn

#main loop
while True:
    rlist, wlist, elist = select.select([s],[],[])
    for sock in rlist:
        conn = accept(sock)
        rlist.append(conn)
    for sock in rlist[1:]:
        listen(sock)


# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('localhost', 1234))
# s.listen(5
