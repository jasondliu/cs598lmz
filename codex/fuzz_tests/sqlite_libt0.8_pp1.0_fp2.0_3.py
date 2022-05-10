import ctypes
import ctypes.util
import threading
import sqlite3
import os
import signal
import sys
import string
import re
from subprocess import Popen,PIPE
import time
import select

#
#  Options to choose from:
#
#    LARGE_PACKET_SIZE       maximum size of a packet (2^14)
#    SMALL_PACKET_SIZE       minimum size of a packet (2^7)
#    NUMBER_OF_PACKETS       number of packets to send per client
#    THREAD_COUNT            number of threads to spawn for client
#    PREPARE_COUNT           number of clients to prepare (including the thread spawning one)
#    CLIENTS_PER_THREAD      number of clients per threads (sum of all this must be < PREPARE_COUNT)
#    NUMBER_OF_TESTS         number of tests to perform (also the number of different packetsizes)
#    SERVER_PORT             port to run on
#

LARGE_PACKET_SIZE = 16384
SMALL_PACKET_SIZE = 128
NUMBER_OF_PACKETS = 50
TH
