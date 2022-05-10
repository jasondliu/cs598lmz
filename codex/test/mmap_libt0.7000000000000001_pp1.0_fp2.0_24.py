import mmap
import platform
import subprocess

from collections import defaultdict
from pathlib import Path

from . import config
from . import db
from . import util

def load_sig(sig_path):
    # read signature file
    with open(sig_path) as f:
        signature = f.read()

    # remove comment lines
    signature = '\n'.join(line for line in signature.split('\n') if not line.startswith('#'))

    # remove indentation
    signature = re.sub(r'^\s+', '', signature, flags=re.MULTILINE)

