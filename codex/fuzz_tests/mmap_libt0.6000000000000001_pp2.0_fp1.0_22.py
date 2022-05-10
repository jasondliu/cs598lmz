import mmap
import os
import sys
import time

from . import cli
from . import config
from . import constants
from . import exceptions
from . import ip
from . import utils


_LOG = logging.getLogger(__name__)

_METADATA_KEY_VALUE_SEPARATOR = '='
_METADATA_LINE_SEPARATOR = '\n'
_METADATA_TEMPLATE = '{key}{separator}{value}'
_METADATA_FILE_PATH = '/tmp/metadata.json'
_NIC_SCRIPTS_PATH = '/etc/sysconfig/network-scripts/'
_NETWORK_CONFIG_PATH = '/etc/sysconfig/network'
_NETWORK_SCRIPT = '/etc/sysconfig/network-scripts/ifcfg-{interface}'
_NETWORK_SCRIPT_BACKUP = '/etc/sysconfig/network-scripts/ifcfg-{interface}.{timestamp}'
_PERSISTENT_NET_RULES_FILE = '/etc/udev/rules.d/70-persistent-
