import mmap
import sys
import random
import time

f = open("access_log")

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line

#for i in range(0, 10):
#    print random_line(f)

def random_line_deterministic(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if num % 100 == 0:
        line = aline
    return line

#for i in range(0, 10):
#    print random_line(f)

def random_line_deterministic_mmap(afile):
    s = mmap.mmap(afile.fileno(), 0, prot=mmap.PROT_READ)
    lines = s.split(b"\n")
    for i in range(random.randrange(len(lines))):
        line
