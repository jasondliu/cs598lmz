import select
# Test select.select
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 利用setblocking设置非阻塞
s.setblocking(False)

# connect方法将触发一个异常
try:
    s.connect(("www.baidu.com", 80))
except BlockingIOError:
    print("错误")

# 接下来，需要对这个异常进行处理，不能把异常抛出去。
# 因为这个异常是connect()方法的正常行为，
# 只是在非阻塞模式下，它不会等待
