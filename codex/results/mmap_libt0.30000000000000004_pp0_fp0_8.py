import mmap
import sys
import os
import re
import shutil
import subprocess
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import zipfile
import zlib

from datetime import datetime
from optparse import OptionParser
from subprocess import Popen, PIPE

from buildbot.steps.shell import ShellCommand

# This is a list of tuples (platform, arch, build_type, build_dir,
# target_arch, target_os) that we want to build.
#
# The 'arch' is the architecture of the machine that will be doing the
# build.  The 'target_arch' is the architecture of the built binaries.
#
# The 'build_dir' is the directory that the build will be placed in.
#
# The 'target_os' is the OS that the binaries will run on.  This is
# usually the same as the build machine OS, but on the mac we build
# binaries for mac and linux.
#
# The 'build_type' is the type of build.  This is either
