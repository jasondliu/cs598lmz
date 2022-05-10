import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import subprocess
import time
import threading
import re


# Get the directory of the script itself
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the directory of the root directory of the repository
# (i.e. the directory containing this file and the parent directory)
repo_dir = os.path.join(script_dir, '..')

# Add the repo_dir to the path
sys.path.insert(0, repo_dir)

# Add the script_dir to the path
sys.path.insert(0, script_dir)

# Import some common functions
import common

# Import the stl_utils class
import stl_utils

# Get the test_dir
test_dir = os.path.join(repo_dir, 'tests')

# Get the build_dir
build_dir = os.path.join(repo_dir, 'build')

# Get
