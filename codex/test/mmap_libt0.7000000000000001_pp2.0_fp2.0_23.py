import mmap
import os
import struct
import sys
import time

import numpy as np

import pytest

from glumpy import app, gloo, gl, glm, data, log

from glumpy.transforms import glm
from glumpy.errors import GLError, GLInvalidOperation, GLInvalidValue

from glumpy.graphics.collections import MarkerCollection, PolygonCollection
from glumpy.graphics.collections import PathCollection, Path, Segment
from glumpy.graphics.collections import PointCollection, Polygon
from glumpy.graphics.text import FontManager
from glumpy.graphics.text import GlyphAtlas, GlyphRenderer

from glumpy.app.window import key

# Global variables
window = None

# Globally initialize font-manager
font_manager = None

# Globally initialize glyph-atlas
glyph_atlas = None

# Globally initialize glyph-renderer
glyph_renderer = None

# Globally initialize collections
points = None
paths = None
polygons = None
