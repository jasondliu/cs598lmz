import lzma
lzma.LZMA_AVAILABLE = False
lzma.LZMA_PATH = None

import tempfile
import os
import io
import sys
import shutil
import tarfile
import unittest
from test import support
from contextlib import closing
