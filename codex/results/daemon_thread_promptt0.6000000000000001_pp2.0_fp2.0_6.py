import threading
# Test threading daemon
import time
from pprint import pprint
from collections import deque

import serial
from serial.tools import list_ports
from serial.tools.list_ports_common import ListPortInfo
from serial.serialutil import SerialException

from config import Config
from utils import is_connected, is_port_available, check_connection_status
from utils import get_os_type, get_ports_list, get_port_name, get_port_name_by_desc
from utils import get_port_desc, get_port_desc_by_name, get_serial_port
from utils import get_serial_ports, get_serial_port_by_name, get_serial_port_by_desc
from utils import get_serial_port_name, get_serial_port_desc, get_serial_port_name_by_desc
from utils import get_serial_port_desc_by_name, get_serial_port_info
from utils import get_serial_port_names, get_serial_port_descs, get_serial_port_infos
from ut
