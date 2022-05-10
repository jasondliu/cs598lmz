import threading
# Test threading daemon
# threading.currentThread().setDaemon(True)
# Test logging
logger = logging.getLogger(__name__)

# class Client(threading.Thread):
class Client(object):
    """
    Client for the Jacktrip server.
    """
    # __slots__ = []

    def __init__(self, settings, **kwargs):
        """
        Initialization routine.
        """
        self.settings = settings
        self.client = None

        self.server_ip = None
        self.server_port = None
        self.num_channels = None
        self.num_port = None

        # Parse the settings.
        self.parse_settings(**kwargs)

        # Initialize the server.
        self.initialize()

    def parse_settings(self, **kwargs):
        """
        Parse the settings from the settings file.
        """
        # Parse the settings.
        if 'server_ip' in kwargs:
            self.server_ip = kwargs['server_ip']
        else
