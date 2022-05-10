import socket
import threading
import argparse

# コマンドライン引数の取得
parser = argparse.ArgumentParser(description='Socket Server Example')
parser.add_argument('--port', action="store", dest="port", type=int, required=True)
given_args = parser.parse_args()
port = given_args.port

# ログファイルの設定
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    filename='threaded.log',
                    filemode='a')

# ログ用のクラス
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       
