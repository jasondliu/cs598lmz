import select

class Socket:
    def __init__(self, socket):
        self.socket = socket
        self.buffer = b''
        self.closed = False

    def send(self, data):
        if self.closed:
            raise Exception('Socket is closed')
        self.socket.send(data)

    def recv(self, size):
        if self.closed:
            raise Exception('Socket is closed')
        while len(self.buffer) < size:
            new_data = self.socket.recv(1024)
            if not new_data:
                self.close()
                raise Exception('Socket is closed')
            self.buffer += new_data
        data = self.buffer[:size]
        self.buffer = self.buffer[size:]
        return data

    def close(self):
        if self.closed:
            return
        self.socket.close()
        self.closed = True

    def fileno(self):
        return self.socket.fileno()

    def __enter__(self):
        return self

    def __exit__(
