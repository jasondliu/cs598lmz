import mmap
import re
import subprocess
import sys
import time

#
# globals
#

# log
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

#
# classes
#

class ADB(object):
    def __init__(self, adb_path='adb'):
        self.adb_path = adb_path

    def _run(self, cmd):
        return subprocess.check_output([self.adb_path] + cmd)

    def devices(self):
        return re.findall(r'^(.*?)\s+device\s*$',
                          self._run(['devices']),
                          re.MULTILINE)

    def forward(self, local, remote):
        self._run(['forward', local, remote])

    def forward_remove(self, local):
        self._run(['forward', '--remove', local])

    def forward_remove_all(self):
        self._run(['forward', '--remove-
