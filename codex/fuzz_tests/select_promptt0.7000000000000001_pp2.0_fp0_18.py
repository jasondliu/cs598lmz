import select
# Test select.select()
# def select_test(n):
#     print "select_test(%d)" % n
#     if n==0:
#         import time
#         time.sleep(2)
#         print "Goodbye"
#     else:
#         import sys
#         r,w,e=select.select([sys.stdin],[],[],1)
#         if r:
#             s=sys.stdin.readline()
#             print "Read",s
#         else:
#             print "Timeout"
#         select_test(n-1)
# select_test(3)

# from select import epoll, EPOLLIN
# from socket import socket, AF_INET, SOCK_STREAM
# from time import sleep
# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('', 20000))
# s.listen(5)
# poll = epoll()
# poll.register(s.fileno(), EPOLLIN)
# while True:
#     events = poll.poll(1
