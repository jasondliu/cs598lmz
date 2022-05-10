import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from mpd.base import MPDBase, CommandError, ConnectionError, ProtocolError

class MPDClient(MPDBase):
    def __init__(self):
        super(MPDClient, self).__init__()
    
    def connect(self, host, port):
        super(MPDClient, self).connect(host, port)
    
    def _disconnect(self):
        if self._connection:
            self.close()



if __name__ == '__main__':
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from mpd import MPDClient
    client = MPDClient()
    client.connect('localhost', 6600)
    print client.status()
    #client.play(0)
    print client.playlist()
    client.disconnect()
