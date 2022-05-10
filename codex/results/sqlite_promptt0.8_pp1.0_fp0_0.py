import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
from uuid import getnode as get_mac

sys.path.append("../..")
from core.config_parser import config
from utils.net.mac_addr import MacAddr
from utils.net.ip_addr import IPAddr
from utils.net.ip6_addr import IP6Addr

from core.netns.veth import veth
from utils.errno import errno_name
from xceptions import VeThException, IPException, MacException, DriverException, \
    ContainerException
from utils.net.orte_utils import orte_utils
from utils.net.common import if_indextoname, if_nametoindex, veth_next, \
    get_netns_pid
from core.netns.iface import IFace
from utils.shell import call, call_silent
from utils.sort_utils import sort_ifaces


class VeThContainer(object):

    """
    This class represents the host itself or a container (in future)
    """
    logger = logging.get
