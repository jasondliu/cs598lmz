import socket
import sys
import time
import random

message = sys.argv[1]
channel = sys.argv[2]

servers = [["irc.freenode.net", 6667], ["irc.oftc.net", 6667], ["irc.mozilla.org", 6667]]
current = random.randint(0,len(servers)-1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) > 3:
    port = int(sys.argv[3])
    s.connect((servers[current][0], port))
else:
    s.connect((servers[current][0], servers[current][1]))

s.send("NICK PyBot\r\n")
s.send("USER PyBot PyBot PyBot :PyBot\r\n")
s.send("JOIN %s\r\n" % channel)

while True:
    data = s.recv(1024)
    if data.find('No ident response') != -
