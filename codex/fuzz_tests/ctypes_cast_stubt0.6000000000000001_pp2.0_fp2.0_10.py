import ctypes
ctypes.cast(0, ctypes.py_object).value = 3

import os
import sys
import time
import platform
import socket
import argparse
import json
import requests
import logging
import logging.handlers
from datetime import datetime
from threading import Thread
from threading import Event
from pkg_resources import parse_version
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import SubjectAltNameWarning

from .version import __version__

from .api.config import Configuration
from .api.util import check_os
from .api.util import get_machine_id
from .api.util import get_mac
from .api.util import get_ip
from .api.util import get_netmask
from .api.util import get_gateway
from .api.util import get_dns_servers
from .api.util import get_hostname
from .api.util import get_timezone
from .api.util import get_time
from .api.util import get_ntp_servers

