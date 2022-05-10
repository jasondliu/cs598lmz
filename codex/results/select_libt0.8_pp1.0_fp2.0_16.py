import select
import struct
import threading

class Stats(object):
    """
    Abstract base class for all stats collectors
    """
    
    def __init__(self, url, frequency=2, name=None, server=None, 
        credentials=None):
        """
        Create a new Stats object to collect data from a server.
        """
        if name is None:
            name = "%s:%d" % (url.hostname, url.port)
        self.url = url
        self.frequency = frequency
        self.name = name
        self.credentials = credentials
        self.server = server
        self.stop_event = threading.Event()
        self.running = False
    
    def start(self):
        self.running = True
        self.stop_event.clear()
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
    
    def shutdown(self):
        self.stop_event.set()
        self.thread.join()
        self.running = False
    
   
