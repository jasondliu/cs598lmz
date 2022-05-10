import socket
socket.if_indextoname(3)

import psutil
psutil.net_io_counters(pernic=True)

import psutil
psutil.net_if_stats()

import psutil
psutil.net_connections()

import psutil
psutil.net_connections(kind='inet')

import psutil
psutil.net_connections(kind='inet4')

import psutil
psutil.net_connections(kind='inet6')

import psutil
psutil.net_connections(kind='tcp')

import psutil
psutil.net_connections(kind='tcp4')

import psutil
psutil.net_connections(kind='tcp6')

import psutil
psutil.net_connections(kind='udp')

import psutil
psutil.net_connections(kind='udp4')

import psutil
psutil.net_connections(kind='udp6')

import psutil
psutil.net_connections(kind='unix')

import psutil
psutil.net
