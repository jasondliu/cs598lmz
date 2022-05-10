import codecs
# Test codecs.register_error
import re
# Test re flags argument
import sys
# For sysconfig
# Build-specific modules.
import os
import shutil
import subprocess
import tempfile
import textwrap
import unittest
import warnings
# For several tests
HAVE_DYLD = hasattr(sys, 'getdlopenflags')
# - How to test a script file
# We want to run libregrtest on the generated script, but before we do so,
# the script must be able to run standalone.  There are a couple of ways
# to do this:
#  - Move it to a temporary directory where its imports will work.
#    This requires making the script relocatable, by using an
#    absolute pathname for its directory.
#  - Add the current directory to sys.path.
#  - Play shenanigans with __main__ and sys.modules, to make the
#    script believe it's in __main__.
TEST_HOME = os.path.dirname(os.path.abspath(__file__))
# Relative to TEST_HOME.
