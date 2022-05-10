import socket
socket.if_indextoname(2)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

'''
Get hostname
'''
import socket

hostname = socket.gethostname()
print(hostname)

ip_address = socket.gethostbyname(hostname)
print(ip_address)

'''
Get ip address
'''
import socket

ip_address = socket.gethostbyname('google.com')
print(ip_address)

'''
Get fqdn(fully qualified domain name)
'''
import socket

fqdn = socket.getfqdn('google.com')
print(fqdn)

'''
Get service name
'''
import socket

service_name = socket.getservbyport(80)
print(service_name)

'''
Get service port
'''
import socket

service_port = socket.gets
