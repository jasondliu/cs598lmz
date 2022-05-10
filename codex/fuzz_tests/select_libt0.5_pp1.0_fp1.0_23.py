import selectors
import socket
import sys
import time

# 定义连接的元组
request_queues = {}
message_queues = {}

# 定义超时时间
timeout = 20

# 定义接收数据的最大字节数
max_recv = 4096

# 定义接收到数据时，发送的响应
response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""

# 定义处理异常的函数
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    message_queues[conn] = queue.Queue()
    request_queues[conn] = queue.Queue()
   
