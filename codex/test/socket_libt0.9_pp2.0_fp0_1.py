import socketserver
import logging
import os

class FTPServer(socketserver.ThreadingTCPServer):
    host_port:tuple

    def __init__(self,host_port,handler):
        self.host_port = host_port
        # 先父类初始化后再子类初始化
        super().__init__(self.host_port,handler)

    def run_server(self):
         self.serve_forever()


