import sys, threading

def run():
    port = sys.argv[2]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], int(port)))
    while True:
        s.send(sys.stdin.readline())

def main():
    port = sys.argv[2]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', int(port)))
    s.listen(1)
    (client, address) = s.accept()

    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

    while True:
        print(client.recv(4096))

if __name__ == "__main__":
    main()
