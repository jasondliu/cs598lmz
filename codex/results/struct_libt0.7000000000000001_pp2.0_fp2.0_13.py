import _struct
from _struct import *
import socket
import os
import sys
import ctypes
import uuid
import ssl

FLOW_CTRL_RECEIVE	= (1 << 0)
FLOW_CTRL_TRANSMIT	= (1 << 1)
FLOW_CTRL_ALL		= FLOW_CTRL_RECEIVE | FLOW_CTRL_TRANSMIT

class hid_rdp_flow_ctrl(Structure):
    _fields_ = [
        ("flags", c_uint32),
        ("start_offset", c_uint32),
    ]

class hid_rdp_req(Structure):
    _fields_ = [
        ("flow_ctrl", hid_rdp_flow_ctrl),
    ]

class hid_rdp_rep(Structure):
    _fields_ = [
        ("flow_ctrl", hid_rdp_flow_ctrl),
        ("max_hid_payload", c_uint16),
    ]

class hid_rdp_protocol(Structure):
    _fields_ = [
