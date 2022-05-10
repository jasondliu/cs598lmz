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


class FTPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                    logging.error("客户端断开连接")
                    break
                data_str = data.decode("utf-8")
                if data_str == "quit":
                    break
                print("客户端:",data_str)
                self.request.send(data)
           
