import select
import struct

def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def create_socket(dest):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto("", (dest, 54545))
    return sock


def send_file(sock, file_name, dest):
    data_size = os.path.getsize(file_name)
    sock.sendto("file:%s:%d" % (file_name, data_size), (dest, 54545))
    f = open(file_name, "rb")
    for piece in read_in_chunks(f):
