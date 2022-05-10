import ctypes
ctypes.cdll.LoadLibrary('libpysupport.so')

import os
import sys
import getopt
import subprocess
import shutil

def run_cmd(cmd):
	print "Running command:",cmd
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	(stdout, stderr) = p.communicate()
	if p.returncode != 0:
		print "Error running command:",cmd
		print "     stdout:",stdout
		print "     stderr:",stderr
		sys.exit(1)
	return stdout

def usage():
	print "Usage: %s [OPTIONS]" % os.path.basename(sys.argv[0])
	print ""
	print "OPTIONS:"
	print "  --help, -h"
	print "    Print this help message."
	print "  --version, -v"
	print "    The version of the package."
	
