import socket
socket.if_indextoname('3')

'''

#发送ICMP数据报
'''
import socket

send_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
send_socket.sendto("", ("127.0.0.1", 0))

