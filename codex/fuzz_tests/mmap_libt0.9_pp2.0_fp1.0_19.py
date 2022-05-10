import mmap
import os
import os.path
import shutil
import signal
import struct
import tempfile
import time
import typing

try:
    import lzma
except ImportError:  # pragma: no cover
    from backports import lzma

# pylint: disable=import-error
try:
    import _thread as thread
except ImportError:
    import threading as thread
try:
    import readline
except ImportError:
    import pyreadline as readline
# pylint: enable=import-error


tag_base = u"tag:%s:" % __name__
tag_locks = tag_base + "locks:"
tag_class_stat = tag_base + "class:Status"
tag_class_unit_state = tag_base + "class:UnitState"
tag_class_global = tag_base + "class:Global"
tag_class_journal = tag_base + "class:Journal"
tag_class_command = tag_base + "class:Command"
tag_class_stat = tag_base + "class:Stat"


