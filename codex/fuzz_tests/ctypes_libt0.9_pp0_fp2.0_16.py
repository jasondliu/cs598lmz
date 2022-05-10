import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)


class Dos_Attack(object):

    def __init__(self, server_IP):
        self.server_IP = server_IP

    def generate(self):
        s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        #s.connect(self.server_IP, 80)
        packets = str
