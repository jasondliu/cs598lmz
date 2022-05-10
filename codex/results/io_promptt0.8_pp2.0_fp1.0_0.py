import io
# Test io.RawIOBase for use in forward compatibility for Python 3
# where io is an abstract class.
try:
    from io import RawIOBase as IO
except ImportError:
    IO = file

import os
import pwd
import re
import signal
import smtplib
import socket
import sys
import tempfile
import threading
import time


from oslo_log import log as logging
from oslo_utils import excutils
from oslo_utils import strutils
from oslo_utils import timeutils
from oslo_utils import units
import six

from nova.i18n import _LE, _LI, _LW
from nova.openstack.common import loopingcall

LOG = logging.getLogger(__name__)

_FILE_CACHE = {}

SMTP_PORT = 25

FLAGS = flags.FLAGS
flags.DEFINE_string('rootwrap_config',
                    '/etc/nova/rootwrap.conf',
                    'Path to the rootwrap configuration file to use for '
                    'running commands as root.')
flags.DEFINE_string('
