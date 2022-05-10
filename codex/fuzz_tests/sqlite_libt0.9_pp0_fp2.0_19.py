import ctypes
import ctypes.util
import threading
import sqlite3
import time
import re
import math
import xml.etree.ElementTree as ET

from pymobility.models.mobility import *

# To print just time in a log message except for PrintLevel.ALL
log_timer = Timer()

class RadioModel(object):
    '''
    The class is a radio model base class that defines the common interfaces for radio models.

    :class:`RadioModel` is a base class for all radio models. Radio models provide radio signal propagation through radio channels, including 
    1. packet reception;
    2. packet loss due to attenuation, external noise, and interference;
    3. packet reception delay;
    4. the creation of a propagation trace file;
    The radio models provide two types of reception:
    1. all-or-nothing reception based on the received signal strength with regard to the values of transmission power and the received signal threshold;
    2. probabilistic reception based on the probability of successful packet transmission;

    Users can inherit :class:`RadioModel` to create their own customized radio models. When developing the customized radio model, users can choose from the two
