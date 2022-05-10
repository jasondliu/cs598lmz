import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import re
import sys
import time
import signal
import socket
import select
import logging
import logging.handlers
import threading
import traceback
import subprocess
import collections

from . import util
from . import config
from . import net
from . import log
from . import proxy
from . import dnslib
from . import checkip
from . import dnsproxy
from . import dnsserver
from . import dnsserver2
from . import dnsserver3
from . import dnsserver4
from . import dnsserver5
from . import dnsserver6
from . import dnsserver7
from . import dnsserver8
from . import dnsserver9
from . import dnsserver10
from . import dnsserver11
from . import dnsserver12
from . import dnsserver13
from . import dnsserver14
from . import dnsserver15
from . import dnsserver16
from . import dnsserver17

