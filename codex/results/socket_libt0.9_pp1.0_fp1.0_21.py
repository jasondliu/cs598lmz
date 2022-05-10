import socket
allok='127.0.0.1'
#allok = socket.gethostbyname(socket.gethostname())
print "[+] Using IP address : ",allok
 
for i in range(1,254):
 
    ip=allok + "." + str(i)
     
    print "Scanning ", ip
         
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    if sock.connect_ex((ip,135)):
          print "Port 135 closed\r"
    else:
        print "[+] Port 135 open : ", ip
        sock.close()
