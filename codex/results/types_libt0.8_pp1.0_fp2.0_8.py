import types
types.TracebackType = type(None)
import os
import sys
import subprocess
import shutil
import glob
import re
import json

# Suppress the warning:
# "DEPRECATION: The default format will switch to columns in the future.
# You can use --format=(legacy|columns) (or define a format=(legacy|columns)
# in your pip.conf under the [list] section) to disable this warning."
# ...until pip sorts this out
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module='pip')

PYTHON_MAJORVER = sys.version_info[0]

if PYTHON_MAJORVER == 2:
    from io import open  # pylint: disable=redefined-builtin

if PYTHON_MAJORVER == 2:
    import ConfigParser as configparser
    import urllib2
    import HTMLParser
    input = raw_input  # pylint: disable=redefined-builtin
else:
    import configparser
    import ur
