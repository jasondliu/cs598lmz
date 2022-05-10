import mmap
import os
import re
import sys
import tempfile
import time

from . import utils
from . import _core

# TODO:
# - add a way to specify the output directory
# - add a way to specify the output file name
# - add a way to specify the output file format
# - add a way to specify the output file size
# - add a way to specify the output file quality
# - add a way to specify the output file type
# - add a way to specify the output file width
# - add a way to specify the output file height
# - add a way to specify the output file resolution
# - add a way to specify the output file color space
# - add a way to specify the output file depth
# - add a way to specify the output file compression
# - add a way to specify the output file orientation
# - add a way to specify the output file color profile
# - add a way to specify the output file metadata
# - add a way to specify the output file background color
# - add a way to specify the output file border color
# - add a way to specify the output file border width
