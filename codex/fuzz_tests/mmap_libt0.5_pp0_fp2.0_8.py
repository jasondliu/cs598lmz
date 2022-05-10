import mmap
import struct
import sys
import time
import threading

from mavlink.mavlinkv10 import MAVLink_heartbeat_message
from mavlink.mavlinkv10 import MAVLink
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink.dialects.v20 import ardupilotmega as mavlink2

# Global variables
global mavlink_data
mavlink_data = {}


class MAVLink_data():
    def __init__(self):
        self.mavlink_data = {}
        self.mavlink_data['timestamp'] = 0
        self.mavlink_data['type'] = 0
        self.mavlink_data['autopilot'] = 0
        self.mavlink_data['base_mode'] = 0
        self.mavlink_data['custom_mode'] = 0
        self.mavlink_data['system_status'] = 0
        self.mavlink_data['mavlink_version'] = 0
