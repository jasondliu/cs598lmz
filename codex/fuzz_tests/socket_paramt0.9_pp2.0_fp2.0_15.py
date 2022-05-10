import socket
socket.if_indextoname(24)

import netifaces as ni

ips = ni.ifaddresses('en0')
ip = ips[ni.AF_INET][0]['addr']

print(ip)

import subprocess
import SocketServer
from socket import gethostname, gethostbyname
import time
from threading import Thread
import random
from SocketServer import ThreadingMixIn
import os
import sys
from Queue import Queue
import cv2.cv as cv 
import cv2
from math import *
from dronekit import *
from datetime import datetime
import time
import socket
from math import *

from picamera.array import PiRGBArray
from picamera import PiCamera
from pymavlink import mavutil
import math
from socket import *

from os import *
from mavproxy.tools.lib import stats


#from dronekit import connect, VehicleMode, Vehicle, LocationGlobal, LocationGlobalRelative
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
import socket
import struct
import re



