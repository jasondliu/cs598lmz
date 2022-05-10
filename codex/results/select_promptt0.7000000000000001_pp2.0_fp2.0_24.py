import select
# Test select.select()
# 和select.poll()一样
# 最后一个参数是超时，默认为None
# 如果没有事件发生，阻塞
# 如果有事件发生，立马返回
# 如果超时，超时后立马返回
#
# 因为需要把socket转换为file descriptor
# 所以返回值是三个列表
# 可读，可写，异常

from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 0))
s.
