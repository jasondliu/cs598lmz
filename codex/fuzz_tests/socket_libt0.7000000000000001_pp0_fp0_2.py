import socket


def get_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return sock


def get_host():
    return socket.gethostbyname(socket.gethostname())


def get_port():
    return 4321


def run_serv():
    sock = get_socket()
    sock.bind((get_host(), get_port()))
    sock.listen(1)
    conn, addr = sock.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        conn.send(data)  # echo
    conn.close()


def run_cli():
    sock = get_socket()
    sock.connect((get_host(), get_port()))
    while True:
       
