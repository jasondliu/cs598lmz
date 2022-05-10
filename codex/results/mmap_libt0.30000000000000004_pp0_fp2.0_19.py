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
SDK_URL = 'http://dl.google.com/android/android-sdk_r%s-linux.tgz'

# This is the base URL for the SDK.  We download the latest SDK from here.
SDK_BASE_URL = 'http://dl.google.com/android/android-sdk_r%s-%s.zip'

# This is the base URL for the NDK.  We download the latest NDK from here.
NDK_BASE_URL = 'http://dl.google.com/android/ndk/android-ndk-r%s-%s.zip'

# This is the base URL for the ANT.  We download the latest ANT from here.
ANT_BASE_URL = 'http://archive.apache.org/dist/ant/
