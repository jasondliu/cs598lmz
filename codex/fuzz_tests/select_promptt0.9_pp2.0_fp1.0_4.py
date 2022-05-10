import select
# Test select.select() used by socketserver
import socketserver

HOST = ""
PORT = 50007
NUM_MSG = 100

def server(test_sock):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print("Connected by", addr)
    for i in range(NUM_MSG):
        rd, wr, ex = select.select([conn, test_sock], [conn], [], 1)
        if conn in rd:
          msg = conn.recv(1024)
          print("server received: ", msg)
        if test_sock in rd:
          cmd = test_sock.recv(1024).decode("utf-8")
          if cmd == "send":
            print("server sending")
            conn.send(br"test message")
