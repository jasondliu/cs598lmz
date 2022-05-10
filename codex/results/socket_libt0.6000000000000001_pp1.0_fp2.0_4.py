import socket

from pyroute2.config import AF_BRIDGE
from pyroute2.netlink import NetlinkError
from pyroute2.netlink.rtnl import ifinfmsg
from pyroute2.netlink import NLM_F_DUMP
from pyroute2.netlink.rtnl import RTM_GETLINK
from pyroute2.netlink.rtnl import RTM_NEWLINK
from pyroute2.netlink.rtnl import RTM_DELLINK
from pyroute2.netlink.rtnl import RTM_SETLINK
from pyroute2.netlink.rtnl import RTM_GETLINKINFO
from pyroute2.netlink.rtnl import RTM_NEWLINKINFO
from pyroute2.netlink.rtnl import RTM_DELADDR
from pyroute2.netlink.rtnl import RTM_NEWADDR
from pyroute2.netlink.rtnl import RTM_GETADDR
from pyroute2.netlink.rtnl import RTM_SETADDR

