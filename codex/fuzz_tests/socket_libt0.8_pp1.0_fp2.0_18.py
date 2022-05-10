import socket
import collections

def udpserver():
    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpsock.bind(('', 8888))
    while True:
        data, address = udpsock.recvfrom(1024)
        if not data:
            continue
        print data, address
        encode_data = data.decode()
        udpsock.sendto(encode_data, address)


if __name__ == '__main__':
    udpserver()
