import select
# Test select.select() to see if we can receive data.
# Use a timeout of 1 second so we don't block forever if there's no data.
ready = select.select([sock],[],[],1)
if ready[0]:
    data, addr = sock.recvfrom(1024)
    print "received:", data, "from", addr
# if select returned that there is data ready to be read from the socket, then
# we can call recvfrom() to get it.
</code>

