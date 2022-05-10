import select
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9000))

while True:
    socket_list = [sys.stdin, s]
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    for sock in read_sockets:
        if sock == s:
            data = sock.recv(4096)
            if not data:
                print("\nDisconnected from chat server")
                sys.exit()
            else:
                sys.stdout.write(data.decode("utf-8"))
                sys.stdout.write("Command: ")
                sys.stdout.flush()
        else:
            msg = sys.stdin.readline()
            s.send(msg.encode("utf-8"))
            sys.stdout.write("Command: ")
            sys.stdout.flush()
