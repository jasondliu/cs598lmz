import socket
socket.if_indextoname(2)
#'en0'

print "NetworkName: %s" % (socket.getfqdn("8.8.8.8"))
#'dns.google.c
