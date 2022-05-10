import socket
socket.if_indextoname(3)

# socket.gethostname()
socket.gethostbyaddr()
socket.getnameinfo()
socket.getaddrinfo()


import platform
print(platform.uname())



import sys
print(sys.platform)
print(sys.version)


import json
json.dumps({})
json.loads('{}')


import re
re.search(r"\bfoo\b", "bar")


import datetime
datetime.datetime.now().strftime('%Y-%m-%d')



import os
os.path.basename('')
os.path.dirname('')
os.path.join(os.path.dirname(__file__), "templates")
os.path.exists('')
os.path.isfile('')
os.path.isdir('')
os.path.islink('')
os.path.ismount('')
os.path.abspath('')
os.path.realpath('')
os.path.getmtime
