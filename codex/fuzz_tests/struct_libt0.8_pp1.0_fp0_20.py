import _struct
import os
import re
import subprocess
import xml.etree.ElementTree
import uuid

_ifconfig_re = re.compile(r'^[\w]*? flags=\d+<((?:[A-Z]+[\d]*?,)*(?:[A-Z]+[\d]*?))> mtu (\d+)$')
_ifconfig_flags = {
    'BROADCAST': 'broadcast',
    'POINTOPOINT': 'point-to-point',
    'RUNNING': 'running',
    'SIMPLEX': 'simplex',
    'LOOPBACK': 'loopback',
    'MULTICAST': 'multicast',
    'NOARP': 'noarp',
    'ALLMULTI': 'allmulti',
    'PROMISC': 'promisc',
    'NOTRAILERS': 'notrailers',
    'DEBUG': 'debug',
    'UP': 'up',
    'DOWN': 'down',
    'SLAVE': 'slave',
    'MASTER': '
