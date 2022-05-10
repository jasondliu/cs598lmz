import sys, threading

def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((sys.argv[1], int(sys.argv[2])))
    while True:
        sock.send(raw_input("> "))

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', int(sys.argv[2])))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print "> " + data

if __name__ == '__main__':
    if sys.argv[1] == 'localhost':
        threading.Thread(target=listen).start()
        run()
    else:
        threading.Thread(target=run).start()
        listen()
