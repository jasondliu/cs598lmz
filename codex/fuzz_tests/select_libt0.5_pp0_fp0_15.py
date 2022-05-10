import select
import sys
import time

import config
import utils

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((config.HOST, config.PORT))
    print "Listening on port %d" % config.PORT

    last_ping = 0
    last_print = 0
    clients = {}

    while True:
        readable, _, _ = select.select([sock], [], [], 1)
        if readable:
            data, addr = sock.recvfrom(1024)
            data = data.split()
            if data[0] == "PING":
                if data[1] == "REQ":
                    sock.sendto("PING REP", addr)
                elif data[1] == "REP":
                    clients[addr[0]] = time.time()
            elif data[0] == "QUIT":
                if data[1] == "REQ":
                    sock.sendto("QUIT REP", addr)
                elif data[1]
