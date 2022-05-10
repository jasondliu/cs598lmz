import _struct
import hashlib
import json
import random
import re
import shutil
import tempfile
import textwrap

from contextlib import ExitStack
from unittest import mock, skipUnless

import primitives.cube
import primitives.cylinder
import primitives.cone
import primitives.sphere
import primitives.polyhedron
import primitives.torus
import primitives.wedge
import primitives.extrusion

RES_DIR = os.path.dirname(__file__)
OPENSCAD_EXE = "openscad"

class DummyCamera:
    def __init__(self, eye=None, center=None, up=None, angle=None):
        self.translation = center and np.array(center) - np.array(eye)
        self.isometric = angle is None
        self.angle = angle or 90

class DummyScene:
    def __init__(self, eye=None, center=None, up=None, angle=None,
                 size=320, origin=[0,0,0], extras=None, **kw
