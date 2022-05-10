import mmap
import struct
import serial
import ast
import time
import serial.tools.list_ports

from threading import Lock
from threading import Thread
from threading import Condition
from queue import Queue
from queue import Empty

from globals import *
from remoteconfig import *
from buttons import *
from display import *
from hardware import *
from networks import *

#
#
#
class  App:
  def __init__(self, remoteConfig, hardwareConfig, networkConfig, buttonConfig, displayConfig):
    self.m_remoteConfig = remoteConfig
    self.m_hardwareConfig = hardwareConfig
    self.m_networkConfig = networkConfig
    self.m_buttonConfig = buttonConfig
    self.m_displayConfig = displayConfig

    self.m_shmem = None
    self.m_serial = None
    self.m_network = None

    self.m_lock = Lock()
    self.m_condition = Condition(self.m_lock)

    self.m_running = True

    self.m_networkCommand = None
    self
