import socket
# Test socket.if_indextoname
socket.if_indextoname(0)
# Test socket.if_nameindex
socket.if_nameindex()
# Test socket.if_nametoindex
socket.if_nametoindex('lo0')

# Test subprocess.Popen
import subprocess
p = subprocess.Popen(['ls'])
p.wait()

# Test time.clock_getres
import time
time.clock_getres(time.CLOCK_REALTIME)

# Test urllib.request
import urllib.request
urllib.request.urlopen('https://www.python.org').read()

# Test xmlrpc.client
import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:9999')
s.ping()
