import _struct
import _socket
import time

# --------------------------------------------------------------------------

def _CheckIP(ip):
    if not ip:
        return False
    # 正则匹配
    pat = "^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$"
    if not re.match(pat, ip):
        return False
    return True

def _CheckPort(port):
    if not port:
        return False
    if not isinstance(port, int):
        return False
    return True

# --------------------------------------------------------------------------

class TcpClient(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = None

    def start(self):
        if not _CheckIP(self.ip) or not _CheckPort(self.port):
            print ("ip or port error!")
