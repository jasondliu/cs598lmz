import socket
import sys

#input the ipaddress with port
host = "10.0.0.1"
port = 9999

#create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, port))
    print("[+]Connection established")
    sock.close()
except socket.error, msg:
    print("[-]Exception occured: " + str(msg))
</code>
Above is what I have written and this is my output

My problem is I am not able to see the string "[-]Exception occured: " + str(msg)".
Please help me to sort this.


A:

You have the variable named <code>host</code>, but you use the word <code>host</code> in your program:
<code>host = "10.0.0.1"
# ...
try:
    sock.connect((host, port))
    print("[+]Connection established")
    sock.close()
except socket.error, host:
#
