from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i", 1)
import sys

print(sys.version)
print(s.size)

import subprocess

def run_cmd(cmd):
    child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return child.communicate()

if __name__ == "__main__":
    out, err = run_cmd("ps -ef | grep python")
    print("out: %s \nerr : %s" % (out, err))

import os

print(os.path.abspath("."))

print(os.name)

print(os.environ)
print(os.environ.get("PATH"))

print(os.path.abspath("test.py"))
print(os.path.split(os.path.abspath("test.py")))
print(os.path.splitext(os.path.abspath("test.py")))

import time


def time
