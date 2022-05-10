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
ANDROID_SDK_URL = 'http://dl.google.com/android/android-sdk_r20.0.3-linux.tgz'

# Path constants. (All of these should be absolute paths.)
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
SDK_DIR = os.path.join(THIS_DIR, '..', '..', '..', 'third_party', 'android_tools', 'sdk')
NDK_DIR = os.path.join(THIS_DIR, '..', '..', '..', 'third_party', 'android_tools', 'ndk')
SDK_TOOLS_DIR = os.path.join(SDK_DIR, 'tools')
SDK_PLATFORM_TOOLS
