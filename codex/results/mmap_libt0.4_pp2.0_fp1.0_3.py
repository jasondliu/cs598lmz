import mmap
import os
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.etree.ElementTree
import xml.parsers.expat

from lib.core.common import Backend
from lib.core.common import checkFile
from lib.core.common import checkOptions
from lib.core.common import checkRoot
from lib.core.common import dataToStdout
from lib.core.common import getLocalIP
from lib.core.common import getRemoteIP
from lib.core.common import getUnicode
from lib.core.common import isListLike
from lib.core.common import isNoneValue
from lib.core.common import isNumPosStrValue
from lib.core.common import isTechniqueAvailable
from lib.core.common import isWindowsDriveLetterPath
from lib.core.common import normalizePath
from lib.core.common import ntToPosixSlashes
from lib.core.common import openFile
from lib.core.common import parseTargetDirect
from lib.core.common import parseTargetUrl
from
