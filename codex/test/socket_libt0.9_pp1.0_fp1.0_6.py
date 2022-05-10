import socketserver
import time

sys.path.append('..')


class MHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("connected from:", self.client_address)
        # self.request.close()
        db_conn = sqlite3.connect("work.sql")
        data = self.request.recv(102400)
