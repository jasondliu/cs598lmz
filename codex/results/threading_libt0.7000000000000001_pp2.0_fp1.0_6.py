import threading
threading.stack_size(4*1024*1024)

import sys, os, re, time
import getopt

from os import listdir
from os.path import isfile, join

from ctypes import *

from multiprocessing import Pool
from multiprocessing.sharedctypes import Value, Array

import httplib, urllib
import hashlib
import json
import uuid

#
#   Configuration
#

#
#   Configuration for the input directory
#

#   Where to look for input files
inputDir = 'input'

#   Specifies if the input directory is a relative or absolute path
#inputDirIsRelative = False
inputDirIsRelative = True

#   Specifies if we should skip files that have already been processed
#skipFilesThatHaveBeenProcessed = True
skipFilesThatHaveBeenProcessed = False

#   Specifies if we should skip files that have already been
#   uploaded to the API endpoint
#skipFilesThatHaveBeenUploaded = True
skipFilesThatHaveBeenUploaded = False

#   Spec
