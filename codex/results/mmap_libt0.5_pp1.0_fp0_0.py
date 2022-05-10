import mmap
import os
import re
import subprocess
import sys
import threading
import time
import traceback
import xml.dom.minidom
import zlib

from ganeti import compat
from ganeti import constants
from ganeti import errors
from ganeti import locking
from ganeti import netutils
from ganeti import pathutils
from ganeti import serializer
from ganeti import utils
from ganeti import workerpool
from ganeti import objects
from ganeti import ssconf
from ganeti import hypervisor
from ganeti import netutils
from ganeti import query
from ganeti import rpc
from ganeti import runtime
from ganeti import ssh
from ganeti import vcs
from ganeti import qlang


#: Default timeout for an SSH connection
SSH_CONNECT_TIMEOUT = 60

#: Default timeout for a command
SSH_COMMAND_TIMEOUT = 600

#: Default timeout for a command with a progress
