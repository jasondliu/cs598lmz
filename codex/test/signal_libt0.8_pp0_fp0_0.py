import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# from lib import common
from lib.client_core import ClientCore

class MessageSender(ClientCore):
    
    def __init__(self):
        ClientCore.__init__(self, "MessageSender")
        self.status = False
        
