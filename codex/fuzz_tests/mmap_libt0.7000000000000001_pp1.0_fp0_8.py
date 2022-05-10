import mmap
import os
import re

from fcntl import ioctl
from io import StringIO

from vmm import get_vmm
from vmm import VMM, VMMCapability

class VMMParser(object):
    """
    Parses the output of vmmctl -l
    """
    def __init__(self, vmm):
        self.vmm = vmm
        self.vm_list = []
        self.vm_macs = {}
        self.vm_pids = {}
        self.vm_names = {}

    def check_vmm(self):
        """
        Check to see if the vmm is the one we have
        """
        if self.vmm.vmmctl_name not in os.listdir("/dev"):
            raise Exception("VMMCTL not found: %s" % self.vmm.vmmctl_name)

        try:
            vmmctl = open("/dev/" + self.vmm.vmmctl_name, "r")
        except OSError as e:
            raise Exception
