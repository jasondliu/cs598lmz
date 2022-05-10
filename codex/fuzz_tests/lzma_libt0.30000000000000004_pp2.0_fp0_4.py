import lzma
lzma.LZMAError

import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
import urllib.parse
import uuid
import xml.etree.ElementTree as ET

from . import config
from . import util
from . import version

#
# Constants
#

# The URL to the server.
SERVER_URL = "https://www.googleapis.com/chromewebstore/v1.1/items"

# The URL to the server for publishing.
PUBLISH_URL = "https://www.googleapis.com/upload/chromewebstore/v1.1/items"

# The URL to the server for uploading a new version.
UPLOAD_URL = "https://www.googleapis.com/upload/chromewebstore/v1.1/items/%s/uploads"

# The URL to the server for publishing a new version.
PUBLISH_UPLOAD_URL = "https://www.googleapis.com/
