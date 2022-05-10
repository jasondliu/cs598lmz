import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-infinite-threads
class MyThread(threading.Thread):
    def run(self):
        while True:
            print("MyThread")

class MyThreadClient(MyThread):
    def run(self):
        import socket
        import time
        import sys
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((sys.argv[1], int(sys.argv[2])))
            s.sendall(b"Hello, world")
            time.sleep(1)
            data = s.recv(1024)
            print('Received', repr(data))
        except BrokenPipeError as e:
            print('Broken pipe error')
        finally:
            s.close()

class MyThreadServer(MyThread):
    def run(self):
        import socket
        import sys
        import time
        # Create a TCP/IP socket
        sock = socket.socket(socket.
