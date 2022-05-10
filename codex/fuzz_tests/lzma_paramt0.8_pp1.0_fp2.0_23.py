from lzma import LZMADecompressor
LZMADecompressor
from bz2 import BZ2Decompressor
BZ2Decompressor
from zlib import Decompress
Decompress
# password for the file is infected

import os, sys
import re
import string
from argparse import ArgumentParser
import zipfile
import fnmatch
import shutil
from os import walk

from shutil import copyfile
from getpass import getpass
from subprocess import call, check_call
from tempfile import TemporaryFile
from os import remove


from pandas import *
from lxml.etree import parse, parseString

from os import listdir
from os.path import isfile,join,isdir
from fnmatch import fnmatch
import glob

from os import walk
import os.path
from os.path import basename
import shutil
#from pprint import pprint
from time import time, localtime
from time import strftime
from pyfasta import Fasta

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet.IUPAC import unambiguous_
