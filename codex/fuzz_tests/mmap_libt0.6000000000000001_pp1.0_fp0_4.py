import mmap
import os
import sys
import time
import traceback

from typing import Dict, List, Optional, Set, Tuple

from . import enums
from . import exceptions
from . import parser
from . import util
from . import version


try:
    from . import _hci as hci
except ImportError as e:
    import atexit
    import subprocess

    # Attempt to compile and load the C extension, if possible.
    import platform

    import shutil
    import tempfile

    _, extension = os.path.splitext(__file__)
    temp_path = tempfile.mkdtemp()
    temp_file = os.path.join(temp_path, "hci" + extension)
    try:
        shutil.copyfile(__file__, temp_file)
        subprocess.check_call([sys.executable, temp_file, "build_ext", "--inplace"])
        shutil.copyfile(temp_file, __file__)
    except Exception as e:
        print(
            "Could not compile C extension
