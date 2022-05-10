import ctypes
import ctypes.util
import threading
import sqlite3
import json
import Queue
import time
import logging
import syslog
import traceback
import base64
import os
import platform
import sys
import hashlib
import subprocess

# Message Severity
AL_INFO = 0
AL_ERROR = 1

# Message Types
AL_CONNECT = 0
AL_DISCONNECT = 1
AL_RADIO_STATUS = 2
AL_RADIO_NACK = 3
AL_RADIO_RECEIVED = 4
AL_MSAC_STATUS = 5
AL_MSAC_MOVED = 6
AL_REQ_REMOTE_CONNECT = 7
AL_CANCEL_REMOTE_CONNECT = 8
AL_RADIO_REMOTE_RECEIVED = 9
AL_COMMISSIONING_STATUS = 10
AL_MSAC_REMOTE_RECEIVED = 11
AL_RADIO_TRANSMIT = 12
AL_MSAC_TRANSMIT = 13

# MSAC Status
MSAC_STATUS_OFF = 0
MSAC_STATUS_ON
