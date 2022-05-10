import socket
# Test socket.if_indextoname() and socket.if_nameindex()
import subprocess
import tempfile
import time

import jinja2

from . import GEXF
from . import p2p_graph
from . import testkit
from . import version
from .ipaddress_util import print_ipv4dotted


logger = logging.getLogger(__name__)

# for future usage - if ifndef THEN dump-trust-graph.py
def conf_ifndef(if_name):
    """
    match IFDEF(6) and IFNDEF(6) from OpenBSD
    https://man.openbsd.org/man6/if_ndp.6#IFDEF
    \*}
    \* define \fIif\fR
    \*.It Fl _
    \* enable parameter groups
    \*
    """
    regex = re.compile(r'(\s+)#\s*define IFNDEF_')
    return re.search(regex, if_name) is None


class OpenBSDTools(object):
    """
    The
