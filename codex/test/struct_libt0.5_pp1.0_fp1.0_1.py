import _struct

class ModbusClient(object):
    def __init__(self, host, port=502, timeout=10, unit_id=1):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.unit_id = unit_id

    def _send_request(self, function, address, value=None, count=None):
        request = self._build_request(function, address, value, count)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        sock.connect((self.host, self.port))
        sock.send(request)
        response = sock.recv(1024)
        sock.close()
        return response

    def _build_request(self, function, address, value=None, count=None):
        if function == 1:
            request = self._read_bits(address, count)
        elif function == 2:
            request = self._read_bits(address, count)
