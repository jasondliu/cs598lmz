import gc, weakref

from gimpfu import *

import re
import os
import sys

sys.path.append(os.path.dirname(__file__))
from lib.py.gimp_utils import *

#===============================================================================

def create_new_layer(image, width, height, name):
    """Create a new layer with the given parameters"""
    layer = gimp.Layer(image, name, width, height,
                       RGB_IMAGE, 100, NORMAL_MODE)
    layer.fill(BACKGROUND_FILL)
    image.add_layer(layer, 0)
    return layer

#===============================================================================

def create_text_layer(image, text, size, font):
    """Create a new text layer with the given parameters"""
    # create a new layer and fill it with white
    layer = create_new_layer(image, image.width, image.height, "text")
    # add the text
    pdb.gimp_text_fontname(image, layer, 0, 0, text, size, True, size,
                           PIXELS
