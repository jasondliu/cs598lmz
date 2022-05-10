import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import zipfile

from optparse import OptionParser

# This is not really used yet.
ANDROID_SDK_VERSION = 'r16'

# The default is to build with Clang.
ANDROID_TOOLCHAIN_VERSION = '4.6'

# The default is to build with GCC 4.6.
ANDROID_NDK_VERSION = 'r8e'

# The default is to build with GCC 4.6.
ANDROID_NDK_TOOLCHAIN_VERSION = '4.6'

# The default is to build with GCC 4.6.
ANDROID_NDK_GCC_VERSION = '4.6'

# The default is to build with Clang.
ANDROID_NDK_CLANG_VERSION = '3.1'

# The default is to build with GCC 4.6.
ANDROID_NDK_
