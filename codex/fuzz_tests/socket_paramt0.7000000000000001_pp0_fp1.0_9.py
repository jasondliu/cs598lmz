import socket
socket.if_indextoname(1)

#get current ip address
socket.gethostbyname(socket.gethostname())

#get current ip address, in my case it is 192.168.43.64
socket.gethostbyname_ex(socket.gethostname())

#get host name from ip address
hostname = socket.gethostname()    
ip_address = socket.gethostbyname(hostname)    
print("Hostname :  ",hostname)    
print("IP Address : ",ip_address) 

#check host is active or not
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
print("Connected to google")
s.close()

#for any kind of error
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
print("Connected to google")
s.close()
except:
    print("could not connect!")

#connect via proxy

