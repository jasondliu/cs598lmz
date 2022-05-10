import select
# Test select.select to see how it works

# Create a list of sockets
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind(("localhost", 1234))
lsock.listen(5)

# Create a UDP socket
usock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
usock.bind(("localhost", 1234))

sockList = [lsock, usock]

while True:

    rlist, wlist, xlist = select.select(sockList, [], sockList, 1)
    
    # sockets are readable (incoming data)
    for s in rlist:
        # New connection
        if s == lsock:
            conn, addr = lsock.accept()
            print "New connection from {0}".format(addr)
            sockList.append(conn)
        # UDP traffic
        elif s == usock:
            buf, addr = s.recvfrom(1024)
            print "Received packet from {0} with data {
