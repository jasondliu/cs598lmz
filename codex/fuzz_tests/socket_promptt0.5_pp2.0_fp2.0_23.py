import socket
# Test socket.if_indextoname()
import sys
import time
import traceback

from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import OctetString

from yunohost.diagnosis import Diagnoser
from yunohost.utils.network import get_interfaces
from yunohost.utils.network import get_public_ip
from yunohost.utils.network import get_public_ipv6
from yunohost.utils.network import get_public_ip_from_pool
from yunohost.utils.network import get_public_ipv6_from_pool
from yunohost.utils.network import is_ipv6_enabled
from yunohost.utils.network import is_ipv6_ula_enabled
from yunohost.utils.network import is_ipv6_ula_autoconf_enabled
from yunohost.utils.network import is_ipv6_ula_autoconf_available
from yunohost.utils.network import is_ipv6
