import socket
socket.if_indextoname(3)

>>> import socket
>>> socket.if_indextoname(3)
'en1'
>>> socket.if_nametoindex('en1')
3
>>> socket.if_indextoname(2)
'lo0'
>>> socket.if_nametoindex('lo0')
2
>>> socket.if_indextoname(1)
'lo0'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import socket
>>> socket.gethostbyname('www.google.com')
'216.58.216.196'
>>> socket.gethostbyname('www.baidu.com')
'220.181.38.148'
>>> socket.gethostbyaddr('216.58.216.196')
('dfw25s10-in-f4.1e100.net', [], ['216.58.216.196'])
>>> socket.gethostbyaddr('220.181.38.148')
('220.181.38.148.bc.googleusercontent.com', [], ['220.181.38.148'
