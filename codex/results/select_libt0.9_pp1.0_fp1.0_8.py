import selectors
import sys
import json
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 11000))
s.listen()


def get_cores():
    try:
        return int(subprocess.check_output("cat /proc/cpuinfo | grep processor | wc -l", shell=True))
    except:
        return 1


cores = get_cores()


def loop():
    print("loop")

    def next_connection():
        server_events.unregister(s)

        conn, addr = s.accept()
        conn.setblocking(False)

        client_events.register(conn, selectors.EVENT_READ, new_data)

    def new_data(conn):
        print("new_data")
        data = conn.recv(1000)
        print("data = '{}'".format(data))
        if data:
            conn.sendall(b"Hello\n")
        else:
            conn.close()
            client
