import types
types.ClassType = type

import os, os.path
import sys
import re
import sys, traceback
import random
import shutil
import time
import copy
import tempfile
import logging
import argparse
import itertools
import optparse
import fnmatch
import subprocess
from collections import Counter

from Bio.Seq import Seq
from Bio import SeqIO
from Bio import SearchIO
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord

from multiprocessing import Process, Queue, Manager
from Queue import Empty

###############################
## Command line argument parser
###############################

#Many references have this little google-only command line parser:
#https://code.google.com/p/comline/
#Could be combined/reduced like this:
#https://code.google.com/p/comline/source/browse/comline/ComLine.py
#Used in:
#https://code.google.com/p/comline/source/browse/examples/simple.py

#Arg
