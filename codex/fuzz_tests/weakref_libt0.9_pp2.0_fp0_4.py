import weakref

connection_list = []  #定义一个全局变量存储每个客户端连接，用一个列表存储
class ChatServer(asyncore.dispatcher):  #自定这ChatServer类，继承自asyncore.dispatcher
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('',9999))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        print ('Connection from ' + repr(addr[0]))
        ChatHandler(conn, self, addr)  #实例化一个新的ChatHandler

class ChatHandler(asyncore.dispatcher_with_send):  #
