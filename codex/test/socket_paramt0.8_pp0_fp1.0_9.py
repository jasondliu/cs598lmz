import socket
socket.if_indextoname(6)

socket.if_nametoindex("eth0")

socket.getaddrinfo("www.baidu.com", 80, 0, 0, socket.IPPROTO_TCP)

socket.gethostbyname("cuiwei.top")
socket.gethostbyname_ex("cuiwei.top")

socket.gethostname()
socket.getfqdn()

import ssl
ssl_ = ssl.create_default_context()
print(ssl_)
ssl.get_server_certificate(("www.baidu.com", 443))

import os

os.getcwd()
os.chdir("/")
os.getcwd()
os.listdir("/")

os.mkdir("/tmp/tmp")
os.listdir("/")
os.rmdir("/tmp/tmp")
os.listdir("/")

os.makedirs("/tmp/tmp/tmp")
os.listdir("/")
os.removedirs("/tmp/tmp/tmp")
os.listdir
