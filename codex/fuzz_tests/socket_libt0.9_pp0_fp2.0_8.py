import socket

class Livestreamer(object):
    def __init__(self):
        self.Servers = ['127.0.0.1']
        self.Port = 4021
        self.socket = None
        self.Bcast = True
        self.Connect()

    def Connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if self.Bcast:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket = sock

    def Send(self, packet):
        self.Connect()
        for server in self.Servers:
            self.socket.sendto(str(packet), (server, self.Port))
        self.socket.close()

    def StopStream(self, streamid):
        packet = 'S:%s' % (streamid)
        self.Send(packet)

    def StartStream(self, streamid, url):
        packet = 'L:%s:%s' % (stream
