import mmap
import sys
import os
import re
import time
import datetime
import time
import subprocess
import sys

def main(argv):
    if len(argv) != 3:
        print("Usage: python3 "+argv[0]+" <log_file> <output_file>")
        sys.exit(1)
    log_file = argv[1]
    output_file = argv[2]
    f = open(log_file, "r")
    fout = open(output_file, "w")
    for line in f:
        if "TOTAL" in line:
            fout.write(line)
            break
    f.close()
    fout.close()

