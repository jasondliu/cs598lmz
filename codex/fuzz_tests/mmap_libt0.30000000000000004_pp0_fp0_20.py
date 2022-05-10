import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib2

from optparse import OptionParser

# Global variables
#
# The following variables are used to control the behavior of the script
#
#  - g_verbose: if True, print verbose messages
#  - g_debug: if True, print debug messages
#  - g_dry_run: if True, do not actually execute anything
#  - g_quiet: if True, do not print anything
#  - g_force: if True, force the operation
#  - g_ignore_errors: if True, ignore errors
#  - g_interactive: if True, ask for confirmation before executing
#  - g_color: if True, use colors
#  - g_colors: dictionary of colors
#  - g_default_color: default color
#  - g_default_style: default style
#  - g_styles: dictionary of styles
#  - g_default_format: default format
#  - g_formats:
