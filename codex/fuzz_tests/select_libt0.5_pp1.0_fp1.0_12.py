import select
import socket
import sys
import threading
import time
import traceback

from wpactrl.common import *
from wpactrl.wpa_ctrl import *
from wpactrl.wpa_ctrl_exception import *

class WpaCtrl:
    """
    A class for communicating with the wpa_supplicant daemon.
    """

    def __init__(self, ifname=None):
        """
        Construct a WpaCtrl object.

        Arguments:

        ifname -- The interface name to use (e.g., "wlan0")
        """
        self.ifname = ifname
        self.attached = False

    def attach(self):
        """
        Attach to the wpa_supplicant daemon.
        """
        if self.attached:
            return
        self.ctrl = wpa_ctrl_open(self.ifname)
        if self.ctrl is None:
            raise WpaCtrlException("Unable to open connection to wpa_supplicant")
        self.attached = True

    def detach
