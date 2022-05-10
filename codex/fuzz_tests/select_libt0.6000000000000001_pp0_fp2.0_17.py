import select, os, sys
import time


def main():
    # server address
    SERVER_ADDRESS = (HOST, PORT) = '', 8888

    # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind socket to server
    sock.bind(SERVER_ADDRESS)
    # listen for connection
    sock.listen(REQUEST_QUEUE_SIZE)
    # create poller
    poller = select.epoll()
    # register server socket
    poller.register(sock.fileno(), select.EPOLLIN)

    try:
        while True:
            # wait for I/O
            events = poller.poll(TIMEOUT)
            for fileno, event in events:
                # server socket
                if fileno == sock.fileno():
                    connection, address = sock.accept()
                    print('Client connected:', address)
                   
