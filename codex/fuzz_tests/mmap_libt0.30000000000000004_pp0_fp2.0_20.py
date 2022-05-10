import mmap
import os
import re
import sys
import time
import traceback

from . import utils
from . import config
from . import constants
from . import exceptions
from . import log
from . import paths
from . import process
from . import registry
from . import services
from . import system
from . import udev
from . import vbox
from . import vminfo
from . import vmnet

#-----------------------------------------------------------------------------

class VM(object):
    """
    A virtual machine.
    """

    def __init__(self, name, vm_type=None, vm_info=None, vm_config=None):
        """
        Initialize a VM object.

        @param name: The name of the VM.
        @param vm_type: The type of the VM.
        @param vm_info: A VMInfo object.
        @param vm_config: A VMConfig object.
        """
        self.name = name
        self.vm_type = vm_type
        self.vm_info = vm_info
        self.vm_config = vm_config
        self
