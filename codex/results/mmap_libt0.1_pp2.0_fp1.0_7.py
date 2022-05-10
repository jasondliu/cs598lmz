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

# This is not really used anymore.
ANDROID_SDK_URL = 'http://dl.google.com/android/android-sdk_r22.0.1-linux.tgz'

# Path constants. (All of these should be absolute paths.)
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
SDK_DIR = os.path.join(THIS_DIR, 'android-sdk-linux')
NDK_DIR = os.path.join(THIS_DIR, 'android-ndk-r8e')
SDK_TOOLS_DIR = os.path.join(SDK_DIR, 'tools')
SDK_PLATFORM_TOOLS_DIR = os.path.join(SDK_DIR, 'platform-tools')
SDK_BUILD_TOOL
