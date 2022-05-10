import mmap
import os
import fcntl
import struct
import socket
import ctypes

from .basetypes import *

IPV4_DEFAULT_GW_FILE = "/proc/net/route"
HOSTNAME_FILE = "/proc/sys/kernel/hostname"
INTERFACES_FILE = "/proc/net/dev"

# Hack to resolve the path, if the file is moved.
# os.path.realpath() would have been easy, but iproute2 (3.18.0) doesn't give the
# absolute path in /proc/net/ip_mr_cache.
PROC_DIR = os.path.dirname(os.path.abspath(os.path.join(os.path.curdir, "proc", "1", "cmdline")))

MROUTE_VIF_FILE = PROC_DIR + "/net/ip_mr_vif"
MROUTE_CACHE_FILE = PROC_DIR + "/net/ip_mr_cache"

# The input and output flags for BPF filters.
# They are defined in the
