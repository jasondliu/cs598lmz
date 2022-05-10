import socket
import time
import platform
import sys
import struct
import getopt
import thread
import threading
import ConfigParser

from prometheus_client import start_http_server, Gauge, Summary
from prometheus_client.core import CounterMetricFamily, GaugeMetricFamily

# globals
sock = None
server_port = 0

# prometheus metrics
prom_config_error = Gauge('prom_config_error', 'Config errors', ['name', 'config'])

# prometheus metrics
prom_udp_error = Gauge('prom_udp_error', 'UDP errors', ['name', 'message'])
prom_udp_packets_received = Gauge('prom_udp_packets_received', 'UDP packets received', ['name'])

# prometheus metrics
prom_tcp_error = Gauge('prom_tcp_error', 'TCP errors', ['name', 'message'])
prom_tcp_packets_received = Gauge('prom_tcp_packets_received', 'TCP packets received', ['name'])


