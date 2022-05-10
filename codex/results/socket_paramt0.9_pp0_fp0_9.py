import socket
socket.if_indextoname(1)

import os
print os.popen("netsh interface ip show config").read()
#import socket
#name=socket.gethostname()
print socket.gethostbyname('localhost')
