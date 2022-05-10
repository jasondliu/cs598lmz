import socket
socket.if_indextoname(3)

# 'lo'

socket.gethostname()

# 'ip-172-31-21-196'

socket.gethostbyname(socket.gethostname())

# '172.31.21.196'

socket.gethostbyname_ex(socket.gethostname())

# ('ip-172-31-21-196', [], ['172.31.21.196'])

socket.gethostbyname_ex(socket.gethostname())[2][0]

# '172.31.21.196'

socket.gethostbyname(socket.gethostbyname_ex(socket.gethostname())[2][0])

# '172.31.21.196'

socket.gethostbyaddr(socket.gethostbyname_ex(socket.gethostname())[2][0])

# ('ip-172-31-21-196.us-west-1.compute.internal',
#  ['ip-172-31-21-196.us-west-1.compute.internal'],
