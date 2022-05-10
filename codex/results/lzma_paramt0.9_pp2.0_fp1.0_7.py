from lzma import LZMADecompressor
LZMADecompressor.memlimit = 2147483648

import sys
import traceback



class Server(object):
    def __init__(self,port,verbose=False):
        # Initialize the socket.
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.s.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
        self.port = port
        self.s.bind(('',port))
        self.s.listen(5)
        self.verbose = verbose
        print('[status] Listening on port %d' % self.port)


    def ServeForever(self):
        self.Proc = Process(target=self.ListeningLoop,args=())
        self.Proc.daemon = True
        self.Proc.start()
        signal.signal(signal.SIGINT
