import socket
import sys
import time
import threading
import os
import signal
import subprocess
import random
import string
import re
import argparse

# Global variables

# The port number to use for the server
port = 0

# The number of threads to use for the server
threads = 0

# The size of the buffer to use for the server
buffer = 0

# The number of connections to use for the server
connections = 0

# The number of bytes to use for the server
bytes = 0

# The number of seconds to run the server
seconds = 0

# The number of seconds to sleep between each connection
sleep = 0

# The number of seconds to sleep between each request
request_sleep = 0

# The number of seconds to sleep between each response
response_sleep = 0

# The number of seconds to sleep between each request and response
request_response_sleep = 0

# The number of seconds to sleep between each response and request
response_request_sleep = 0

# The number of seconds to sleep between each request and response
request_response_sleep = 0


