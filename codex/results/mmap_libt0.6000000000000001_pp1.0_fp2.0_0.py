import mmap
import os

from jinja2 import Template

from config import *

from utils import *
from utils import __version__

from output import *

from fileformat import *

from subprocess import Popen, PIPE

from ctypes import *

from capstone import *
from capstone.arm import *

from keystone import *
from keystone.keystone import *

# from pefile import *

def main():
    parser = argparse.ArgumentParser(description="A static analysis tool for iOS.")
    parser.add_argument("-v", "--version", help="show version", action="store_true")
    parser.add_argument("-a", "--arch", help="specify architecture, support armv7, armv7s, arm64, arm64e", type=str)
    parser.add_argument("-b", "--base", help="base address of binary", type=str)
    parser.add_argument("-i", "--ida", help="launch ida pro, support ios and macos", action="store
