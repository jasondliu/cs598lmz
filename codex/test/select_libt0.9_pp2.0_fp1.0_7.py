import select
from arch import i386

from vtrace.errors import *
from vtrace.breakpoints import *
from vtrace.notifiers import *

# Some globals which disallow attaching to
# self and setting breakpoints on the program
# we're attaching from!
ATTACH_SELF_OK = False
DBG_SELF_BPS_OK = False

class AttachException(Exception):
    pass

def osGetPidByName(name):
    output = subprocess.check_output(["pidof", name])
    if len(output) > 0:
        return int(output)
    else:
        return None

def osForceAttach(pid):
    return os.system('kill -9 %d >/dev/null 2>&1'%pid)

