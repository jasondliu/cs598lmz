import socket
import sys
import time
import threading
import Queue
import os
import signal

from optparse import OptionParser

from mote import Mote
from mote import MoteDefines
from mote import MoteState
from mote import MoteConnector
from mote import MoteConnectorSerial
from mote import MoteConnectorUdp
from mote import MoteConnectorTcp
from mote import MoteConnectorNull

from openvisualizer.moteConnector import MoteConnector

import logging
log = logging.getLogger('MoteConnector')
log.setLevel(logging.DEBUG)
log.addHandler(logging.NullHandler())

class MoteConnector(object):
    '''
    \brief The MoteConnector class provides an abstraction for connecting to
           a mote.
    '''
    
    def __init__(self,moteProbe_handler,moteProbe_serialport=None,moteProbe_udpport=None,moteProbe_tcpport=None):
        
        # store params
        self.moteProbe
