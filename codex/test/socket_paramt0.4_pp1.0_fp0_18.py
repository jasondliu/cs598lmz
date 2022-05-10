import socket
socket.if_indextoname("1")

#get ip address from interface name
import socket
socket.if_nameindex()
socket.if_nametoindex("lo")

#get the MAC address of a network interface
import uuid
hex(uuid.getnode())

#get the name of the host
import socket
socket.gethostname()
socket.getfqdn()

#get the IP address of the host
import socket
socket.gethostbyname(socket.gethostname())

#get the MAC address of the host
import uuid
hex(uuid.getnode())

#get the users environment
import os
os.environ
os.getenv("HOME")

#get the current date and time
import datetime
datetime.datetime.now()

#get the current process id
import os
os.getpid()

#get the current user id
import os
os.getuid()

#get the current working directory
import os
os.getcwd()

#get the size of a file
import os
os.path.getsize("test.txt")
