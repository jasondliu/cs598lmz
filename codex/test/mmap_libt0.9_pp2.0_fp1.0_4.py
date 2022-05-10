import mmap
import re
from subprocess import Popen, PIPE, run
from tempfile import TemporaryDirectory
import time
from typing import List, Optional


def find_process(filename: str) -> Optional[int]:
    """Find ID of a process with given filename."""
    for line in mmap.mmap(0, 0, '/proc/self/maps'):
        # according to `man 5 proc`
        # the file readable by all processes is required here,
        # accessible by both kernel and userspace
        # (unlike `task/<pid>/maps`)
        line = line.decode("utf-8").split(' ')
        _, _, file, _, _ = line
        if re.sub(r'\[.*\]', '', file) == filename:
            break
    else:
        return None
    return int(line[4])  # pid


def is_running(filename: str) -> bool:
    """Check if a process with given filename is running."""
    if find_process(filename) is None:
        return False
   
