import socket
import time
import threading

def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input("请输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定本地信息
    udp_socket.bind(("", 7890))
    # 3.获取对方的ip和port
    dest_ip = input("请输入
