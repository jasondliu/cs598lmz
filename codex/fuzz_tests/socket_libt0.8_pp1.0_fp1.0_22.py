import socket

def main():
    #创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定本地信息
    local_addr = ("",9000)

    tcp_socket.bind(local_addr)

    #让默认的套接字由主动变为被动
    tcp_socket.listen(128)

    #等待客户端连接
    new_socket,new_addr = tcp_socket.accept()
    print("%s连接上了"%str(new_addr))

    #接收
    receive_data = new_socket.recv(1024)
    print("接收到的数据：%s"%receive_data.decode("utf-8"))

    #
