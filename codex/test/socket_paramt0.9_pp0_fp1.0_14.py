import socket
socket.if_indextoname(5)

# dns info:
print('*** DNS name lookup: ***')
import socket
for host in ['www.siecn.com', 'www.sina.com', 'www.cctv.com', '192.168.1.1', 'www.baidu.com']:
    try:
        print('%s: %s' % (host, socket.gethostbyname(host)))
    except socket.error as err_msg:
        print('%s: %s' % (host, err_msg))
