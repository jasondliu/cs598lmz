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
    print cmd
    return system(cmd)

def cc_so(path):
    cmd = 'gcc -fpic -shared -Wall -W -Werror -g -O2 -c ' + path
    print cmd
    return system(cmd)

def ld(paths, output):
    if len(paths) == 1:
        cmd = 'gcc -Wall -W -Werror -g -O2 ' + paths[0] + ' -o ' + output
    elif len(paths) > 1:
        cmd =
