import mmap
import os
import re
import sys
import zlib

from afl import fs, util

FUNC_RE = re.compile(
    '^([a-f0-9]+)\s+[a-f0-9]+\s+([^\[]+)\s*(\[[^\]]+\])?.*$')

syscall_number = {
    "bproc": "bproc_syscall",
    "gnu": "stub_syscall",
    "ia32": "ia32_syscall",
    "kvm": "kvm_syscall",
    "lguest": "lguest_syscall",
    "openrisc": "openrisc_syscall",
    "parisc": "parisc_syscall",
    "power": "syscall_entry",
    "s390": "s390_syscall",
    "sh": "sys_call_table",
    "sparc": "sparc_syscall",
    "tile": "sys_call_table",
    "um": "stub_sys
