import select

if sys.version_info < (3, 3, 0):
    import subprocess32 as subprocess
else:
    import subprocess


class UnixClient(object):
    def __init__(self, address, timeout=2.0):
        self.address = address
        self.timeout = timeout
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        self.socket.connect(address)

    def execute(self, cmd):
        """
        Send a command to the server and receive the output.
        """
        cmd = cmd.encode('utf-8')
        cmd_len = struct.pack('!i', len(cmd))
        message = cmd_len + cmd
        self.socket.sendall(message)
        ret = self._recvall()
        return ret.decode('utf-8')

    def _recvall(self):
        sock = self.socket
        buf = io.BytesIO()
