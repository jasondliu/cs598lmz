import socket
socket.if_indextoname(5)

import psutil

net_io = psutil.net_io_counters(pernic=True)['en0']
