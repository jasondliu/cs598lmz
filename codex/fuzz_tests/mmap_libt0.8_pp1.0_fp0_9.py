import mmap
import os
import subprocess
from utils import *

def setup():
    """
    Build the nop module
    """
    os.chdir(os.path.join(os.path.dirname(__file__), 'nop'))
    subprocess.check_call(['make'])
    os.chdir(os.path.join(os.path.dirname(__file__), '..'))

def target(v):
    """
    Build a target with a ``main()`` function that writes the values 1 to 10
    to the stdout file descriptor.
    """

    v.add_arg('--file-path', type=str, default='foo.txt')

    v.add_arg('--function', type=str, default='main')
    v.add_arg('--source-filename', type=str, default='foo.c')

    v.add_arg('--disk-filename', type=str, default='foo.disk')
    v.add_arg('--addresses', nargs='*', type=hex_number, default=[
