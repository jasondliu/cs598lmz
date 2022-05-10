import ctypes
import ctypes.util
import threading
import sqlite3
import re
import os

PIDGIN_SUPPORTED = "2.10.0"
PIDGIN_MIN_SUPPORTED = "2.9.0" #<-- 2.8.0 support dropped at 2.6
version_pattern = r"\s+?(([0-9]+)\.([0-9]+)\.([0-9]+))"
info_pattern = "<td>Protocol</td><td>(.+?)</td></tr><tr><td>Account"

def string_before(value, a):
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]

def string_after(value, a):
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

def string_segment(value, a,
