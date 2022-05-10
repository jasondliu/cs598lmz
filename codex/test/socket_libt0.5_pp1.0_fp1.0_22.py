import socket
import threading

def send_msg(udp_socket):
    """发送消息"""
    while True:
        send_data = input("请输入要发送的消息：")
        udp_socket.sendto(send_data.encode("utf-8"),("127.0.0.1", 7890))

def recv_msg(udp_socket):
    """接收消息"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))

def main():
    """完成udp聊天器的整体控制"""
    # 1.创建套接字
