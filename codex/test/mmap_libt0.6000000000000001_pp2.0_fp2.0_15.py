import mmap
import sys
import os
import time
import subprocess
import re
import random
import threading
from multiprocessing import Process
#from multiprocessing.dummy import Process
#from multiprocessing.pool import ThreadPool as Pool
from multiprocessing import Pool

def is_exe(fpath):
	return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

def which(program):
	fpath, fname = os.path.split(program)
	if fpath:
		if is_exe(program):
			return program
	else:
		for path in os.environ["PATH"].split(os.pathsep):
			path = path.strip('"')
			exe_file = os.path.join(path, program)
			if is_exe(exe_file):
				return exe_file

	return None

def check_exe(program):
	if which(program):
		return True
