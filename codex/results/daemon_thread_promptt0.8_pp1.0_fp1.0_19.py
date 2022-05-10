import threading
# Test threading daemon mode

def print_test():
    while True:
        print(strftime("%a, %d %b %Y %H:%M:%S"))
        sleep(1)

t = threading.Thread(target=print_test)
# t.setDaemon(True)
t.start()


# import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)
sock.bind(server_address)
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)

    msg = connection.recv(1)
    print(msg)
    connection.close()
