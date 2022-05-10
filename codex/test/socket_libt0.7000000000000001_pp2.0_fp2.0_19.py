import socket
import threading
import sys

class Sender(threading.Thread):
    ''' A threading class to send messages to the remote end. '''

    def __init__(self, port, host):
        '''
        Create a new sender on the given port and host.

        Args:
            port (int): The port to connect on.
            host (str): The host to connect to.
        '''

        super(Sender, self).__init__()
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try to connect.
        try:
            self.sock.connect((host, port))
            print('Connected to ' + host + ':' + str(port))
        except Exception as e:
            print('Error: ' + str(e))
            sys.exit()

    def run(self):
        '''
        Starts the thread.

        This will prompt for a message to send.
        '''

