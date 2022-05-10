import mmap
import re
import struct
import sys
import time
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment
import yaml

from lib.common.abstracts import Auxiliary
from lib.common.exceptions import CuckooPackageError


class Procmeminfo(Auxiliary):
    """Get information about process memory allocations."""

    def __init__(self, pid=None):
        Auxiliary.__init__(self)
        self.pid = pid
        self.meminfo_path = None

        if self.pid is None:
            self.pid = pid

        if self.pid is None:
            raise CuckooPackageError("No PID specified")

    def _get_procmeminfo_path(self):
        """
        @return: the path to the procmeminfo file
        """
        result = None

        if "linux" in sys.platform:
            try:
                result = "/proc/%d/maps" % int(self.pid)
            except ValueError as e:

