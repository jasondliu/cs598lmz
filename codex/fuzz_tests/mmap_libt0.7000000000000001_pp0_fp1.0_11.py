import mmap
import re
import struct
import sys
from random import randint

from pycrc import Crc
from pycrc.algorithms import Crc8
from pycrc.algorithms import Crc16
from pycrc.algorithms import Crc32
from pycrc.algorithms import Crc64
from pycrc.algorithms import CrcSick
from pycrc.algorithms import Crc8Maxim
from pycrc.algorithms import Crc8Usb
from pycrc.algorithms import Crc8DvbS2
from pycrc.algorithms import Crc8Wcdma
from pycrc.algorithms import Crc8Ebu
from pycrc.algorithms import Crc16CcittFalse
from pycrc.algorithms import Crc16Arc
from pycrc.algorithms import Crc16AugCcitt
from pycrc.algorithms import Crc16Buypass
from pycrc.algorithms import Crc16Cdma2000
from pycrc
