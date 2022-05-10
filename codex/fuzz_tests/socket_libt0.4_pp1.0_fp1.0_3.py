import socket
import time
import threading
import sys

#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#设置端口可重用
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#绑定端口
s.bind(('127.0.0.1',9999))

#用于存储每个客户端的信息
client_list = []

#用于存储每个线程所对应的客户端信息
thread_list = []

#接收客户端请求
def udp_recv():
    while True:
        #接收数据
        data,addr = s.rec
