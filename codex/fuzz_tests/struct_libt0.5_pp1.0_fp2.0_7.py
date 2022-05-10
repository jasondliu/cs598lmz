import _struct

import aiohttp
import aiohttp.web

# The default host to bind to.
DEFAULT_HOST = '127.0.0.1'

# The default port to bind to.
DEFAULT_PORT = 8888

# The default path to the socket file.
DEFAULT_SOCKET_PATH = '/tmp/py-http-server.sock'

# The default maximum number of concurrent connections to allow.
DEFAULT_MAX_CONNECTIONS = 1000

# The default maximum number of bytes to read from a request.
DEFAULT_MAX_REQUEST_SIZE = 1024 * 1024

# The default maximum number of bytes to read from a response.
DEFAULT_MAX_RESPONSE_SIZE = 1024 * 1024

# The default maximum number of bytes to read from a request body.
DEFAULT_MAX_REQUEST_BODY_SIZE = 1024 * 1024

# The default maximum number of bytes to read from a response body.
DEFAULT_MAX_RESPONSE_BODY_SIZE = 1024 * 1024

# The default number of bytes to read from a request
