import socket
socket.if_indextoname('10')
#host_name = socket.gethostname()
host_ip = socket.gethostbyname('192.168.10.164')
print(host_ip)

a = 1
b = 0

while a:
    b = b + 1
    print(b)
    if b == 10:
        a = 0
        print(a)

print('hello')
a = 1
if a == 1:
    print('true')
else:
    print('false')
print('this is my test')
