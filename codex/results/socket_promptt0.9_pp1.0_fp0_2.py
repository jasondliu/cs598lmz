import socket
# Test socket.if_indextoname('4')
# Import NMS packages
from lib.common import check_pid
from nms_config import NMS_LOC
# Import from other NMS modules
from lib.util import mac2eui, ip4_reverse, get_nameservers, get_searchdomain
# Import third party packages
from pyroute2 import IPRoute
from pyroute2.netns.nslink import NSLink
from py2neo import Graph
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

# Load the configuration file
import configparser
config = configparser.ConfigParser()
config.read(NMS_LOC + '/lib/napalm_config.ini')

# Global variables
sdn_request = ('cpu': 'cpu_load', 'memory': 'memory_usage', 'interfaces': 'interfaces')
interfaces_info = []
skip_iface = ('eth0.2', 'lo')
hosts_json = {}
# Defined as a global variable so that the function
