import io
# Test io.RawIOBase for absolute-seek support
import os
import platform
import random
import re
import shutil
import stat
import sys
import tempfile
import time
import unittest
import warnings
import weakref

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

