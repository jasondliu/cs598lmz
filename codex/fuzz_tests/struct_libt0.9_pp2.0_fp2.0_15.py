import _struct
import random
import time
import re
import sys
import copy
import datetime
import logging

def spawn_process(cmd, wait=True):
    """
    Spawn a process.
    """
    if not isinstance(cmd, list):
        raise TypeError("cmd is not a list.")
    try:
        child = subprocess.Popen(cmd)
    except OSError as e:
        raise RuntimeError("Error spawning '%s' process - %s"%(
            ' '.join(cmd), e
        ))
    if wait:
        child.wait()

def check_proc(pid):
    """
    Checks if a pid exists on the current host
    """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True

def is_gzip(filename):
    """
    Returns True if given file is a gzip.
    """
    try:
        with gzip.open(filename) as f:
            f.read(1)
        return True
    except (
