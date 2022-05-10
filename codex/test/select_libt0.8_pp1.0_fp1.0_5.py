import select

# =============================================================================
#
# =============================================================================

class TcpClient():

    def __init__(self, id, host, port, msg, timeout=None):
        self.id = id
        self.host = host
        self.port = port
        self.msg = msg
        self.timeout = timeout
        self.sock = None

    def start(self):
        pass

    def send(self):
        start_time = datetime.now()

        try:
            self.sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
            self.sock.setblocking(0)
            self.sock.send(self.msg)
        except (socket.timeout, socket.error) as e:
            end_time = datetime.now()
            return (self.id, 0, None, end_time - start_time)
        except Exception as e:
            raise

