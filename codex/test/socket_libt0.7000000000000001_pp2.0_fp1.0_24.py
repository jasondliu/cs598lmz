import socket

ip_port = ('127.0.0.1', 8006)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(ip_port)

while True:
    data, addr = sk.recvfrom(1000)
    print("收到数据: ", data)
    print("收到客户端", addr)
    # sk.sendto("data".encode("utf-8"), addr)
sk.close()
