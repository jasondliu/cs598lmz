import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import json
import platform
import argparse
import signal
import re

# https://github.com/tss-ab/python-tss
# https://github.com/tihmstar/libgeneral

def is_digit(s):
    if isinstance(s, int):
        return True
    if isinstance(s, str) and s.isdigit():
        return True
    return False

def is_hex(s):
    if isinstance(s, str) and s.startswith("0x"):
        return True
    return False

def hex_to_int(s):
    if not is_hex(s):
        return None
    return int(s, 16)

def is_dec(s):
    if isinstance(s, str) and s.startswith("0x"):
        return False
    return is_digit(s)

def dec_to_int(s):
    if not is_dec(s):
        return None
    return int(s, 10)
