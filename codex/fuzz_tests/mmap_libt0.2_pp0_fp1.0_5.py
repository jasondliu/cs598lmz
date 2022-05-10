import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib
import urllib2
import urlparse
import zipfile

from optparse import OptionParser

# This is not meant to be a generic tool. It is tailored to the needs of
# the WebKit project.

# FIXME: This script is not robust. It should be rewritten in Python.

# FIXME: This script should be able to download a tarball from a URL.

# FIXME: This script should be able to download a tarball from a local path.

# FIXME: This script should be able to download a tarball from svn.

# FIXME: This script should be able to download a tarball from git.

# FIXME: This script should be able to download a tarball from perforce.

# FIXME: This script should be able to download a tarball from cvs.

# FIXME: This script should be able to download a tarball from mercurial.

# FIXME: This script should be able to download a tarball from
