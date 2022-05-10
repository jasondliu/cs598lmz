import socket
import threading
import time
import sys
from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from enum import Enum
from queue import Queue, Empty
from select import select
from threading import Thread
from typing import List, Tuple, Union
from uuid import UUID, uuid4
from xml.etree import ElementTree as ET

import six
from six.moves import queue
from six.moves.urllib import request, parse

from .upnp_error import UpnpError
from .utils import (  # noqa: F401
    get_free_port,
    get_lan_ip_address,
    get_local_ip_address,
    get_mac_address,
    get_random_udn,
    get_uuid,
    get_xml_text,
    parse_location,
    check_ip_address,
    check_port,
)

# default log level
LOGGER_LEVEL_DEFAULT = logging.ERROR


class UpnpBroadcastResponder(object):
    """
    Broadcast
