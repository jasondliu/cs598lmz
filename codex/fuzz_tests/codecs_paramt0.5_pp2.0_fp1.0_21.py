import codecs
codecs.register_error("strict", codecs.ignore_errors)

import os
import sys
import time
import re
import logging
import datetime
import tempfile
import subprocess
import urllib

from django.conf import settings
from django.core.cache import cache

from PIL import Image, ImageFont, ImageDraw

#===============================================================================

def render_to_image(text, font_path, size, color, background_color,
                    antialias=True, stroke_color=None, stroke_width=0,
                    wrap_width=0, shadow_color=None, shadow_offset=(0, 0),
                    image_type='PNG'):
    """
    Renders the given text to an image.
    
    Returns a file-like object.
    
    'text' is the text to render.
    
    'font_path' is the path to the font to use.
    
    'size' is the font size to use.
    
    'color' is the font color to use.
    
    'background_color' is the background color to use
