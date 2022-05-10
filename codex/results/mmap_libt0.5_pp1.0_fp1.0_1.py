import mmap
import re
import os
import sys
import time
import argparse
import subprocess

# Make sure we have a compatible version of Python
min_python_version = (2, 7)
if sys.version_info < min_python_version:
    print("ERROR: The script requires Python version %d.%d or newer" % min_python_version)
    sys.exit(1)

# Make sure we have a compatible version of setuptools
if int(setuptools.__version__.split(".", 1)[0]) < 18:
    print("ERROR: The script requires setuptools version 18.0 or newer")
    sys.exit(1)

# Make sure we have a compatible version of wheel
if int(wheel.__version__.split(".", 1)[0]) < 0:
    print("ERROR: The script requires wheel version 0.30 or newer")
    sys.exit(1)

# Make sure we have a compatible version of pip
if int(pip.__version__.split(".", 1)[0]) < 6:
    print("ERROR: The script requires pip
