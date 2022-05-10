import socket
import select
import sys

mhost = "127.0.0.10"
mport = 7000
ttl = 1

def get_my_ip():
    try:
        sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        sock.connect( ("8.8.8.8",80) )
        my_ip = sock.getsockname()[0]
        sock.close()
        return my_ip
    except:
        return get_local_ip()

def get_local_ip():
    ip_list = socket.gethostbyname_ex(socket.gethostname())[2]
    if len(ip_list) == 0:
        sock = socket.socket(socket.AF_INET)
        sock.connect(("www.baidu.com",80))
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    else:
        return ip_list[0]

while 1:
    print("组
