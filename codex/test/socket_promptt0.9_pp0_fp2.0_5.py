import socket
# Test socket.if_indextoname and socket.if_nametoindex
#

from test import support
from test.support import os_helper
from test.support.socket_helper import bind_port

set_of_filterable_interfaces = {
    # interfaces that should be filtered out
    'lo', 'lo0', 'docker0', 'docker_gwbridge', 'br-0aa87fbc6165',
    'br-80b3d3e6d8df', 'docker_gwbridge', 'vethf3214c9', 'br-f14eaf6a03b6',
    'docker0', 'veth2f724d6', 'brd+', 'virbr0'}

