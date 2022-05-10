import socket
import sys
import os


def result(directories):
    host = "localhost"
    port = 43003

    sock = socket.socket()
    sock.connect((host, port))
    sock.send(str(directories).encode())
    result = sock.recv(1024).decode()
    sock.close()
    print("Результат работы парсера: " + result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Парсер каталогов")
    parser.add_argument('--dir', nargs='+',
                        help='перечисления каталогов через пробел')
    args = parser.parse_args()
    dirs = set()
    string_dirs = ""
    if not args.dir:
        print("
