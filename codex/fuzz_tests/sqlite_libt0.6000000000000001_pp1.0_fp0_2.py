import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess

#
# list of capabilities
#
capabilities = [
    'CAP_NET_RAW',
    'CAP_NET_BIND_SERVICE',
    'CAP_NET_BROADCAST',
    'CAP_IPC_LOCK',
    'CAP_IPC_OWNER',
    'CAP_SYS_MODULE',
    'CAP_SYS_RAWIO',
    'CAP_SYS_CHROOT',
    'CAP_SYS_PTRACE',
    'CAP_SYS_PACCT',
    'CAP_SYS_ADMIN',
    'CAP_SYS_BOOT',
    'CAP_SYS_NICE',
    'CAP_SYS_RESOURCE',
    'CAP_SYS_TIME',
    'CAP_SYS_TTY_CONFIG',
    'CAP_MKNOD',
    'CAP_LEASE',
    'CAP_AUDIT_WRITE',
    'CAP_AUDIT_CONTROL',
    'CAP_SETFCAP',
