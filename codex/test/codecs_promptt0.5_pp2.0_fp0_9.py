import codecs
# Test codecs.register_error('strict', )
import os
import sys
import time

# This is a hack to make it easier to use the same code for Python 2 and 3.
if sys.version_info[0] == 3:
    unicode = str

