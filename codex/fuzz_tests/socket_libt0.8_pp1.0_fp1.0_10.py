import socket
from select import select


def main():
    """
    获取用户输入，并发送给对方
    """
    # 创建套接字对象默认使用IPv4和TCP协议
    sockfd = socket()
    # 设置端口自动回收
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定地址
    sockfd.bind(("127.0.0.1", 8888))
    # 设置为监听套接字
    sockfd.listen(5)
    # 循环监控列表
    rlist = [sockfd, sys.stdin]
    wlist = []
    xlist = []

