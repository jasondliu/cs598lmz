import mmap
# Test mmap.mmap(-1, 1024*1024*500)
import sys
import os
import re
import subprocess
import platform
import time
import warnings
import threading
import Queue

# path to directory holding this file (assumed to be src/, not /usr/share/doc)
#self.srcdir = sys.path[0]
#sys.path.append(self.srcdir)
#sys.path.append(self.srcdir + "/lib")

#import lib
#import lib.config
#import lib.common
#import lib.threading
#import lib.log
#import lib.exec
#import lib.security
#import lib.net
#import lib.package


# -----------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------

# IMPORTANT: DO NOT MODIFY THIS FILE!
#
# This file contains the global settings for the entire project.
# The configuration file is generated at installation time,
# and is located at /etc/guardianproject/gscript.conf
#

# basedir is used to determine the location of the config file
# the config file should be located at
