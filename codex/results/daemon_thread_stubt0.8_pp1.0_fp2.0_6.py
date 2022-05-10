import sys, threading

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024)
            print('Received', repr(data))


def main():
    threading.Thread(target=run).start()
    while True:
        data = input("> ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(data)

main()
