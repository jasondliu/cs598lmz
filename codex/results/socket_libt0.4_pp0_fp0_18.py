import socket
import sys
import threading
import time

import pytest

from pynetdicom import AE, evt, PYNETDICOM_IMPLEMENTATION_UID, PYNETDICOM_IMPLEMENTATION_VERSION
from pynetdicom.sop_class import (
    CTImageStorage,
    VerificationSOPClass,
)


#debug.debug_file = sys.stdout


class TestAssociationAcceptor(object):
    """Run tests on AE.on_accept"""
    def setup(self):
        """Run prior to each test"""
        self.ae = None
        self.assoc = None

    def teardown(self):
        """Clear any active threads"""
        if self.ae:
            self.ae.shutdown()

        if self.assoc:
            self.assoc.release()

        time.sleep(0.1)

        for thread in threading.enumerate():
            if isinstance(thread, threading._MainThread):
                continue
            try:
                thread._tstate_
