import mmap
import os
import re
import subprocess
import sys
import time

import numpy as np
import psutil

# Get the current script path.
scriptPath = os.path.realpath(__file__)

# Get the directory of this script.
scriptDir = os.path.dirname(scriptPath)

# Change directory to the script directory.
os.chdir(scriptDir)

# Import the script modules.
import file_io
import input_parsing
import memory_profiling
import ram_disk

# Get the arguments.
args = input_parsing.get_args()

# Get the number of processes to run.
nProcesses = args.processes

# Get the number of threads to use.
nThreads = args.threads

# Get the number of minutes to run for.
nMinutes = args.minutes

# Get the file pattern to use for files.
filePattern = args.filePattern

# Get the directory to write files to.
writeDir = args.writeDir

# The file names for the files to
