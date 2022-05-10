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

    # replace tabs with spaces
    signature = signature.replace('\t', ' ')

    # split into lines
    lines = signature.split('\n')

    return lines

def parse_sig(lines):
    # parse signature
    sig_version = lines[0].strip().split()[1]

    assert sig_version == '1'

    sig = {
        'name': lines[1].strip().split()[1],
       
