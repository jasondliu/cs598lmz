import mmap
import os
import sys
import time

from mako.template import Template

# Check python version
if sys.version_info < (3, 0):
    print("ERROR: Python 3 is required to run this script.")
    sys.exit(1)

# Check if we have a valid config
if not os.path.isfile('config.py'):
    print("ERROR: No config file found.")
    sys.exit(1)

# Import config
from config import *

# Check if we have a valid config
if not os.path.isfile('config.py'):
    print("ERROR: No config file found.")
    sys.exit(1)

# Import config
from config import *

# Check if we have a valid config
if not os.path.isfile('config.py'):
    print("ERROR: No config file found.")
    sys.exit(1)

# Import config
from config import *


# Check if we have a valid config
if not os.path.isfile('config.py'):
    print("ERROR: No config
