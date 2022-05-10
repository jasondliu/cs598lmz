import io
class File(io.RawIOBase):
    def __init__(self, sock):
        self.sock = sock
    def readable(self):
        return True
    def readinto(self, b):
        return self.sock.recv_into(b)
    def writeable(self):
        return True
    def write(self, b):
        return self.sock.send(b)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8080))
    # sock.setblocking(False)
    file = File(sock)
    while True:
        data = file.read(1024)
        print(data)
        if not data:
            break
        file.write(data)

if __name__ == '__main__':
    main()
