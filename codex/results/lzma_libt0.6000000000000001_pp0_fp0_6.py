import lzma
lzma.path.append('/usr/lib64/python2.6/site-packages/lzma/')
import xml.etree.cElementTree as ET
import operator
import sys
import os
import re
import random
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    if len(sys.argv) != 3:
        print "Usage: python %s <questions.xml> <output_dir>" % sys.argv[0]
        sys.exit(1)
    questions = ET.parse(sys.argv[1]).getroot()
    output_dir = sys.argv[2]
    if not os.path.exists(
