import mmap
import os
import os.path
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import urlparse
import xml.dom.minidom
import zipfile

# This is a list of the names of the files that are downloaded from the
# Chrome tree. If you add a new file to this list, you need to add it to
# the list of files to delete in the finally clause below, too.
DOWNLOADED_FILES = [
  'chrome.dll',
  'chrome_dll.lib',
  'chrome_dll_a.lib',
  'chrome_dll_debug.lib',
  'chrome_dll_debug_a.lib',
  'chrome_dll_d.lib',
  'chrome_dll_d_a.lib',
  'chrome_dll_d_debug.lib',
  'chrome_dll_d_debug_a.lib',
  'chrome_dll_d_pdb.lib',
  'chrome_dll_d_pdb_a.lib',
  '
