import socket
import os

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1025))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print("Connected to: ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received: ", data)
            conn.sendall(data)
        conn.close()

if __name__ == "__main__":
    main()
