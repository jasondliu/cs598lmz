import weakref
import time
from functools import wraps
from pyroute2 import config
from pyroute2.netlink.exceptions import NetlinkError, NetlinkDecodeError
from pyroute2.netlink.rtnl.capi import capi
from pyroute2.netlink.rtnl.capi import nl_cache_mngr
from pyroute2.netlink.rtnl.capi import nl_socket
from pyroute2.netlink.rtnl import RTNL_GROUPS
from pyroute2.ipdb.transactional import Transactional
from pyroute2.ipdb.transactional import commit_block
from pyroute2.ipdb.transactional import Listener
from pyroute2.netlink import nlmsg

log = logging.getLogger(__name__)


class IPDBError(NetlinkError):
    pass


class Cache(object):
    '''
    Cache class.

    Keeps a copy of the state of a particular cache category.

    When the cache is being instanced, it
