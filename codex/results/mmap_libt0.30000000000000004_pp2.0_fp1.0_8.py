import mmap
import os
import re
import sys
import time

from . import _psutil_posix
from . import _psutil_posix_common
from . import _psutil_mswindows


__extra__all__ = []

# =====================================================================
# --- constants
# =====================================================================


NUM_CPUS = _psutil_posix.get_num_cpus()
BOOT_TIME = _psutil_posix.get_system_boot_time()
# XXX get_system_cpu_times() could return bogus values on Linux
# (https://github.com/giampaolo/psutil/issues/621)
TOTAL_PHYMEM = _psutil_posix.get_total_phymem()
AVAIL_PHYMEM = _psutil_posix.get_avail_phymem()

# =====================================================================
# --- functions
# =====================================================================


def virtual_memory():
    """System virtual memory as a namedtuple."""
    total, free, buffers, shared, _, _ = _psutil_posix.get_sysinfo
