import socket
# Test socket.if_indextoname()
#
# $Id: if_indextoname.py,v 1.4 2003/07/25 12:36:54 wrobell Exp $
#

idx = socket.if_nametoindex('lo')
print 'Index of interface "lo": %d' % idx

nme = socket.if_indextoname(idx)
print 'Name of interface %d: %s' % (idx, nme)

#TODO: test socket.if_nameindex() and socket.if_nametoindex()
