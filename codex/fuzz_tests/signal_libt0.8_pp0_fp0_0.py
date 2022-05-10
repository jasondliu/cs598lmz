import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# from lib import common
from lib.client_core import ClientCore

class MessageSender(ClientCore):
    
    def __init__(self):
        ClientCore.__init__(self, "MessageSender")
        self.status = False
        
    def on_message(self, ws, message):
        print "on message"
        print message
        self.status = True
        
    def on_pong(self, ws, pong):
        # print "pong"
        self.status = True
    
    def is_connection_status(self):
        '''
        response code:
        # 1000, 1008, 1015, 1006: websocket is closed
        # 1011: server side error
        '''
        return self.status

def main(argv):
    client = MessageSender()
    client.start()
    
if __name__ == "__main__":
    main(sys.argv[1:])
