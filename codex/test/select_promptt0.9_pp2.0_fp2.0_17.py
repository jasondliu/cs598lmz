import select
# Test select.select()
# select.select( rlist , wlist , xlist , timeout )
# 监视文件描述符变化
# 1)  rlist监视可读变化
# 2)  wlist监视可写变化
# 3)  xlist监视其他异常
# 4)  元素为socket对象
# 5)  timeout 为超时时间(秒)
        # OS 无法准确时间,只能返回 0
# timeout < 0   阻塞模式
# timeout == 0  非阻塞模式
# timeout > 0   等待时间


import socket
import select

socket_server = socket.socket()
addr = ( 'localhost', 8001 )
# 是
