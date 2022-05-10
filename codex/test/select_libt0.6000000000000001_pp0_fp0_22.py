import selectors
import time
import threading

# 使用selectors模块实现高效的IO事件循环
# selectors模块实现了多路复用IO，可以跨平台使用
# 可以在select/poll/epoll等底层模型之间转换

class MyEventHandler:
    def fileno(self):
        'Return the associated file descriptor'
        raise NotImplemented('must implement')

    def wants_to_receive(self):
        'Return True if receiving is allowed'
        return False

    def handle_receive(self):
        'Perform the receive operation'
        pass

    def wants_to_send(self):
        'Return True if sending is requested'
        return False

    def handle_send(self):
        'Send outgoing data'
        pass

