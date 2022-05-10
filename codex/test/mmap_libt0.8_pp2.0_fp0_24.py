import mmap
import os
import re
import subprocess
import sys

try:
    from fcntl import ioctl
    from termios import *
    from ctypes import *
except ImportError:
    from fcntl import ioctl
    from termios import *
    from ctypes import *

def system(cmd):
    return subprocess.Popen(cmd, shell=True).wait()

def cc(path):
    cmd = 'gcc -Wall -W -Werror -g -O2 -c ' + path
