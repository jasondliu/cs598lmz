from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b)

import gzip
gzip.decompress(b)

import lzma
lzma.decompress(b)

import zlib
zlib.decompress(b)

#!python3
#encoding=utf-8

import os
import sys
import signal
import subprocess

def run_proc(command):
    subprocess.check_call(command, shell=True)

def signal_handler(signum, frame):
    run_proc('kill -9 %s' % os.getpid())

signal.signal(signal.SIGTERM, signal_handler)

run_proc('sleep 10')

print('done')

#!python3
#encoding=utf-8

import os
import signal
import subprocess

subprocess.check_call('sleep 10', shell=True)

print('done')

#!python3
#encoding=utf-8

import os
import signal
import subprocess

subprocess.check_call('sleep 10', shell
