import select
import socket
import sys
import threading
import time
from multiprocessing import Process, Queue
from Queue import Empty

import dpkt
import numpy as np

from common.util import get_local_ip
from common.util import get_mac_address
from common.util import get_packet_size
from common.util import get_packet_time
from common.util import get_protocol_type
from common.util import get_ttl
from common.util import get_window_size
from common.util import is_ipv4
from common.util import is_ipv6
from common.util import is_tcp
from common.util import is_udp
from common.util import is_icmp
from common.util import is_http
from common.util import is_dns
from common.util import is_ftp
from common.util import is_ntp
from common.util import is_ssh
from common.util import is_smtp
from common.util import is_telnet
from common.util import is_pop3
from common
