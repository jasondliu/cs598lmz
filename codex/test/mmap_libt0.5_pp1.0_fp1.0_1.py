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
