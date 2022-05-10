import codecs
codecs.register_error('strict', codecs.ignore_errors)

from distutils.util import strtobool
from io import StringIO
from pyroute2.common import uifname
from pyroute2.common import basestring
from pyroute2.common import basestruct
from pyroute2.common import PY3
from pyroute2.netlink.rtnl.rtmsg import rtmsg
from pyroute2.netlink.rtnl.tcmsg import tcmsg
from pyroute2.netlink.rtnl.ifinfmsg import ifinfmsg
from pyroute2.netlink.rtnl.ndmsg import ndmsg
from pyroute2.netlink.nlsocket import NetlinkSocket
from pyroute2.netlink.rtnl.capi import CAPIMsg
from pyroute2.netlink.rtnl.capi import CAPI
from pyroute2.netlink.exceptions import NetlinkError
from pyroute2.netlink.exceptions import NetlinkHeaderError
from pyroute2.netlink.exceptions import NetlinkMessage
