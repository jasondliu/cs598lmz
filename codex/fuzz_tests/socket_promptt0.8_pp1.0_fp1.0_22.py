import socket
# Test socket.if_indextoname() - run this using 'taskset -c 2 ./ifindextoname'.
# This was written because if_indextoname() was returning ENXIO for index 2 in if.c.
print "Get ifname of index 2:", socket.if_indextoname(2)
#
# Test socket.getservbyport().  Make sure that it actually works.
#
servbyport = {
    80: 'http',
    443: 'https',
    25: 'smtp',
    }
for port, serv in servbyport.items():
    print 'getservbyport(%d)' % port, socket.getservbyport(port)
    # If this fails, you may need to add the service to your /etc/services.
#
# Test socket.getservbyname().  This will catch a number of typos.
#
getservbyname = servbyport.copy()
getservbyname.update({'http': 80, 'https': 443, 'smtp': 25})
for serv, port in getservbyname.items():
    print 'gets
