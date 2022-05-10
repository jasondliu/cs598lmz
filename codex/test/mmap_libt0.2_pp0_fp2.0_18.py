import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from distutils.version import LooseVersion
from functools import partial
from glob import glob
from itertools import chain
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from os.path import join, exists, basename, dirname, abspath, isdir, isfile, realpath, splitext, relpath
from platform import system
from subprocess import Popen, PIPE
from threading import Thread
from time import sleep

