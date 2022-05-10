import socket

def send_data(sock, data):
    """
    Send data to the socket.
    """
    sock.sendall(data)


def recv_data(sock, length):
    """
    Receive data from the socket.
    """
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('socket closed %d bytes into a %d-byte message'
                           % (len(data), length))
        data += more
    return data


def send_message(sock, message):
    """
    Send a message to the socket.
    """
    send_data(sock, struct.pack('>L', len(message)) + message)


def recv_message(sock):
    """
    Receive a message from the socket.
    """
    length_packed = recv_data(sock, 4)
    length = struct.unpack('>L', length_packed)[0]
    return recv
