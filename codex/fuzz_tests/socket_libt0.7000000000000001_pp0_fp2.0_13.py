import socket
import time
import threading

# 打印字典
def printDict(dict):
    print("*"*50)
    print("全部信息")
    print("*"*50)
    for d in dict:
        print(d)
    print("*"*50)

# 打印列表
def printList(list):
    print("*"*50)
    print("全部信息")
    print("*"*50)
    for l in list:
        print(l)
    print("*"*50)

# 主逻辑
def main():
    # 数据
    all_messages = []
    all_users = []

    # 主函数
    def main_func():
        # 创建套接字
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 套
