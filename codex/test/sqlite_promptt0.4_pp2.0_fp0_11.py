import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/var/lib/misc/dnsmasq.leases")

class DnsmasqLeases(object):
    """
    Class to read dnsmasq leases file.
    """
    def __init__(self, leases_file):
        self.leases_file = leases_file
        self.leases = []
        self.lock = threading.Lock()
        self.read()

    def read(self):
        """
        Read the leases file.
        """
        self.lock.acquire()
        try:
            fd = open(self.leases_file, "r")
        except IOError:
            self.lock.release()
            return
        self.leases = []
        for line in fd:
            line = line.split()
            if not line:
                continue
            lease = Lease()
