import threading
threading.stack_size(67108864)

import subprocess
import struct
import os
import sys
import time

# import the user mode driver library
import zed_python as zed

import ctypes
import datetime


# declare a Non-Strict FP SDL Context
ctypes.CDLL('libSDL2-2.0.so.0', mode=ctypes.RTLD_GLOBAL)

# logging import
from pythonosc import osc_message_builder
from pythonosc import udp_client

# communication interface with the Unity application
sender = udp_client.SimpleUDPClient( "127.0.0.1", 50005 )

# logging import
from pythonosc import osc_message_builder
from pythonosc import udp_client

# communication interface with the Unity application
sender = udp_client.SimpleUDPClient( "127.0.0.1", 50005 )

# motion capture communication
mocap_client = udp_client.SimpleUDPClient( "localhost", 54321 )

# video stream communication

