import weakref
import sys
import os
import time


# Class to handle the client side of a port forwarding connection
class PortForwarder(object):
    """
    This class is used to create a port forwarder.
    """
    def __init__(self, parent, connection_id, host, port,
                 local_host, local_port, timeout=1,
                 logger=None, event_handler=None,
                 connection_handler=None,
                 username=None, password=None,
                 private_key=None,
                 private_key_password=None,
                 local_bind_address=None,
                 ):
        """
        Create a port forwarder.

        :param parent: The parent object of this port forwarder.
        :param connection_id: The connection id of this port forwarder.
        :param host: The host to forward to.
        :param port: The port to forward to.
        :param local_host: The local host to forward from.
        :param local_port: The local port to forward from.
        :param timeout: The timeout for the connection.
       
