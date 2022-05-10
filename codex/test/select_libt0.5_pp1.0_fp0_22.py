import select
import socket
import sys
import traceback

from libmproxy import controller, proxy
from libmproxy.proxy.server import ProxyServer

from netlib import tcp, http, certutils
from netlib.exceptions import ProxyConnectionError
from netlib.odict import ODictCaseless
from .. import version
from ..protocol import http as http_protocol
from . import protocol
from . import wsgi
from . import proxy as proxy_module
from . import flow
from . import filt
from . import console
from . import script
from . import eventsequence
from . import addonmanager
from . import versioncheck
from . import proxy_modes
from . import controller as mitmcontroller
from . import stateobject
from . import tnetstring
from . import language


class Options(stateobject.StateObject):
    def __init__(self, **kwargs):
        stateobject.StateObject.__init__(self)
