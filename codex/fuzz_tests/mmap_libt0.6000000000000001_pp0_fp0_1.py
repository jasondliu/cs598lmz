import mmap
import os
import re
import ssl
import subprocess
import sys
import threading
import time
import xml.sax
import xml.sax.handler
import zipfile

import fontTools.ttLib
import fontTools.ttx
import fontTools.unicode

from fontTools.misc.cliTools import makeOutputFileName

__version__ = "0.1.0"

# This is the default output of the "otfinfo -g" command.
# If the output of this command changes, we need to change the code below.
# The code is complicated, because it needs to work with the various
# versions of the OpenType spec, and the various versions of the otfinfo
# command.
#
# The otfinfo -g output has changed over time.
# The changes are:
#   - In OpenType spec 1.5, the "Version" field was added.
#     The "Version" field is not present in the 1.4 spec.
#   - In OpenType spec 1.6, the "GlyphSet" field was renamed to "Glyphs".
