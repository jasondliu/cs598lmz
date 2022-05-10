import _struct

import logging

logger = logging.getLogger(__name__)

# Some constants from the C header files

# from include/linux/input.h

#
# Event types
#
EV_SYN = 0x00
EV_KEY = 0x01
EV_REL = 0x02
EV_ABS = 0x03
EV_MSC = 0x04
EV_SW = 0x05
EV_LED = 0x11
EV_SND = 0x12
EV_REP = 0x14
EV_FF = 0x15
EV_PWR = 0x16
EV_FF_STATUS = 0x17

#
# Synchronization events.
#
SYN_REPORT = 0
SYN_CONFIG = 1
SYN_MT_REPORT = 2
SYN_DROPPED = 3

#
# Keys and buttons
#
KEY_RESERVED = 0
KEY_ESC = 1
KEY_1 = 2
KEY_2 = 3
KEY_3 = 4
KEY_4 = 5
KEY_5
