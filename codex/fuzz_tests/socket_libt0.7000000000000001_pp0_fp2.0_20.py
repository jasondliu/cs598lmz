import socket

if __name__ == '__main__':

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind(('localhost', 8888))

        while True:
            print('waiting data...')
            data, address = server.recvfrom(1024)
            print('received data %s from %s' % (data.decode('utf-8'), address))

            server.sendto(b'Received', address)

    finally:
        print('closing socket')
        server.close()
