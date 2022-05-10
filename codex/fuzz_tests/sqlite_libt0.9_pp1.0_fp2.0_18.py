import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import os
from typing import Type

from . import zvbi
from . import appletalk
from . import dvb
from . import ipproto
from . import iso13818_1
from . import iso13818_6
from . import iso13818_6_dsmcc
from . import mip
from . import network
from . import network_layer
from . import ntp
from . import pid_types
from . import ppp
from . import ppp_chap_msv1
from . import radius
from . import scte35
from . import services
from . import sip
from . import smtp
from . import ssl
from . import tcp
from . import tpg
from . import ts
from . import udp
from . import wsp


########################################################################################################################


def parsed_py_tv(sql_conn: sqlite3.Connection, data: bytes, caplen: int, ts: int, packet_number: int) -> None:
    try:
        parsed_packet = _ParsedPacket(sql_
