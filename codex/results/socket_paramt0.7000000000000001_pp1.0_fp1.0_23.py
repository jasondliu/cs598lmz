import socket
socket.if_indextoname(2)

# Mac OS X
>>> socket.if_indextoname(2)
u'en1'
>>> socket.if_nameindex()
[(1, u'lo0'), (2, u'en1')]

# Windows
>>> socket.if_indextoname(1)
'\\Device\\NPF_{ADB112F9-6E9F-4D5F-9B29-1E4B4BFE29F8}'
>>> socket.if_nameindex()
[(1, '\\Device\\NPF_{ADB112F9-6E9F-4D5F-9B29-1E4B4BFE29F8}')]

# Linux
>>> socket.if_indextoname(1)
'lo'
>>> socket.if_nameindex()
[(1, 'lo'), (2, 'eth1'), (3, 'tap0')]

# FreeBSD
>>> socket.if_indextoname(1)
'lo0'
>>> socket.if_nameindex()
[(1,
