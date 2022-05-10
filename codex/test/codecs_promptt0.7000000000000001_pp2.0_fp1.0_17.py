import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
try:
    codecs.register_error('strict', codecs.strict_errors)
except TypeError:
    pass

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import hashlib
import math
import os
import re
import sys
import threading
import time
import weakref
import xml.etree.cElementTree as ElementTree

