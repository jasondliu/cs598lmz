import socket

#s = socket.socket() # for TCP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # for UPD
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
host = '127.0.0.1'
port = 12331
s.bind((host, port))

while 1:
    d, a = s.recvfrom(1024)
    
    print(d.decode())
    
    d = input(a[0]+ ': ')

    s.sendto(d.encode(), a)

    d = input('Me: ')

    print(d)
