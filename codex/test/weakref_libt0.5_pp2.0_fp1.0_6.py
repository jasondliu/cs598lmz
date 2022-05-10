import weakref
import sys
import os
import time


# Class to handle the client side of a port forwarding connection
class PortForwarder(object):
    """
    This class is used to create a port forwarder.
    """
