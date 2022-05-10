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
import zipfile

from optparse import OptionParser

# This is not really used anymore.
ANDROID_NDK_ROOT = os.environ.get('ANDROID_NDK_ROOT',
                                 '/usr/local/google/home/cduan/android-ndk-r8b')

ANDROID_SDK_ROOT = os.environ.get('ANDROID_SDK_ROOT',
                                 '/usr/local/google/home/cduan/android-sdk-linux')

# The default is to build everything.
BUILD_TARGETS = os.environ.get('BUILD_TARGETS', 'all')

# The default is to build for all architectures.
BUILD_ARCHS = os.environ.get('BUILD_ARCHS', 'arm x86 mips')

# The default is to build for all API levels.
BUILD_APIS =
