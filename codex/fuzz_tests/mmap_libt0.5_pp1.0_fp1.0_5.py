import mmap
import os
import re
import subprocess
import sys
import time
import zipfile

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from . import config
from . import commands
from . import images
from . import reader
from . import writer
from . import utils

from . import config
from . import images
from . import reader
from . import writer
from . import utils


# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

def get_font(font_path, font_size):

    if not os.path.exists(font_path):
        raise Exception("Font file not found: %s" % font_path)

    return ImageFont.truetype(font_path, font_size)


# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

def get_font_size(font, text, max_width, max_height):

    font_size = 1
    while True:
        font_size += 1
        text_size = font.getsize(text)
        if (text_size[0] > max_
