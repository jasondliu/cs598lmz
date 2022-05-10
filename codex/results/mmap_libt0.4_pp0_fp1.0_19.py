import mmap
import os
import re
import shutil
import subprocess
import tempfile
import time

from typing import List, Optional

from . import config
from . import util
from . import version
from . import vmnet
from . import vmnetx
from . import vmprofile
from . import vmsharedfolder


class VirtualMachine:
    """
    A VirtualBox virtual machine.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.vm_dir = os.path.join(config.get_vm_dir(), self.name)
        self.log_dir = os.path.join(self.vm_dir, 'log')
        self.vbox_dir = os.path.join(self.vm_dir, 'VirtualBox VMs')
        self.vbox_file = os.path.join(self.vbox_dir, self.name + '.vbox')
        self.vbox_file_tmp = self.vbox_file + '.tmp'
        self.vbox_file_timestamp =
