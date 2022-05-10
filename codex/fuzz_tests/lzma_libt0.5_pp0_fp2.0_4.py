import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

import sys
import struct
import time
import os
import re
import shutil
import platform
import subprocess

def _detect_platform():
    if platform.system() == 'Windows':
        return 'win'
    elif platform.system() == 'Darwin':
        return 'mac'
    elif platform.system() == 'Linux' and platform.machine() == 'x86_64':
        return 'linux64'
    elif platform.system() == 'Linux' and platform.machine() == 'i686':
        return 'linux32'
    else:
        return None

PLATFORM = _detect_platform()

def _load_config():
    with open('config.py') as f:
        return f.read()

def _get_version():
    config = _load_config()
    m = re.search(r'VERSION\s*=\s*(.+?)\s*$', config, flags=re
