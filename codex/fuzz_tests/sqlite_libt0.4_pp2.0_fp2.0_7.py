import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import datetime
import subprocess
import re
import json

# The following is a hack to get the path of the current file.
# It is necessary because the file is run as a cron job, so
# the current working directory is not the same as the file
# directory.
# See: http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
# Note: this is not a good solution, it is better to use
# the -f option of cron to specify the full path of the
# file.
#
# This is not necessary if the file is run from the command line
# with the full path.
pathname = os.path.dirname(sys.argv[0])        
fullpath = os.path.abspath(pathname)

# The following is a hack to get the path of the current file.
# It is necessary because the file is run as a cron job, so
# the current working directory is not the same as the file
# directory.
# See: http://
