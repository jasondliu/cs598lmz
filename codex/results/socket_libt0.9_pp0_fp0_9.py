import socket

ip_port = ('127.0.0.1', 6666)

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while 1:
    name = input('输入昵称：')
    break

while 1:
    msg = input('输入要发送的信息：')
    msg_send = name + ':' + msg
    sk.sendto(msg_send.encode(), ip_port)
