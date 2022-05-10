import select
import socket
import sys
import time
import traceback
import urllib
import urlparse
import xml.dom.minidom

import gdata.auth
import gdata.client
import gdata.data
import gdata.gauth
import gdata.service
import gdata.urlfetch

# The default timeout for an HTTP request.
DEFAULT_TIMEOUT = 5

# The default number of times to retry a failed HTTP request.
DEFAULT_RETRIES = 2

# The default user-agent for an HTTP request.
DEFAULT_USER_AGENT = 'GData-Python/2.0.18'

# The default content-type for an HTTP request.
DEFAULT_CONTENT_TYPE = 'application/atom+xml'

# The default charset for an HTTP request.
DEFAULT_CHARSET = 'UTF-8'

# The default boundary for an HTTP request.
DEFAULT_BOUNDARY = 'END_OF_PART'

# The default number of seconds to wait before retrying a failed HTTP request.
DEFAULT_DELAY =
