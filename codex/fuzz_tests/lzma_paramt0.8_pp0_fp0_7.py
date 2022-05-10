from lzma import LZMADecompressor
LZMADecompressor()
from sys import argv,exit
from os import popen

# from subprocess import run
# from subprocess import CompletedProcess
# from subprocess import TimeoutExpired
# from subprocess import CalledProcessError
# from subprocess import STDOUT

# from shlex import quote
# from shlex import split
# from shlex import quote_from_shel

from re import compile
from re import findall
from re import MULTILINE
from re import DOTALL

from argparse import ArgumentParser
# from argparse import RawDescriptionHelpFormatter


#==================================================================================================
# Variables
#==================================================================================================

__author__ = "Mauricio M. M. Maciel Junior"
__copyright__ = "Copyright 2020, CodeForces"
__license__ = "GPL"
__version__ = "1.0.1"
__status__ = "Production"

#==================================================================================================
# Functions
#==================================================================================================

# Function to get the current running script name (without extension)
def getScriptName():
	return argv[0].split('.')[0]

