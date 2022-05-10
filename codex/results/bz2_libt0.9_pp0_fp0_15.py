import bz2
bz2.BZ2File.name = lambda self: os.path.basename(self.filename)

import collections
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

from . import version


# Python 2/3 compatibility issues
if sys.version_info[0] >= 3:
    PY2 = False
    PY3 = True
    def b64encode(data):
        if type(data) == str:
            return data.encode('utf-8').decode('latin1')
        else:
            return data.decode('latin1')
    def b64decode(data):
        if type(data) == str:
            return data.encode('latin1').decode('utf-8')
        else:
            return data.decode('utf-8')
    def base64encode(data):
        if type(data) == str:
            return base64.b64encode(data.encode('utf-8')).decode('utf
