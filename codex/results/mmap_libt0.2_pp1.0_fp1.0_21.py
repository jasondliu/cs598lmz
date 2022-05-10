import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom

from BeautifulSoup import BeautifulSoup

from lib.core.common import (
    getUnicode,
    randomRange,
    randomStr,
    readInput,
    singleTimeWarnMessage,
    urldecode,
    urlencode,
)
from lib.core.data import (
    conf,
    kb,
    logger,
    paths,
    queries,
)
from lib.core.enums import (
    CUSTOM_LOGGING,
    HTTP_HEADER,
    HTTPMETHOD,
    PLACE,
    POST_HINT,
    REDIRECTION,
    UNICODE_ENCODING,
    URI_HTTP_HEADER,
)
from lib.core.exception import (
    SqlmapConnectionException,
    SqlmapGenericException,
    SqlmapNoneDataException,
    SqlmapSilentQuitException
