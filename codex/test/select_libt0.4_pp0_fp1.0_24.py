import select
import socket
import sys
import threading
import time

# This is a simple web server that responds to GET requests by sending files
# from the data_files directory.  This directory should be filled with files
# to be sent.

# This server is single-threaded, which means that it will only process one
# request at a time.  This is usually OK when testing, but it is not OK in
# production.  Your assignment is to make this server multi-threaded.

# This server is also blocking, which means that it processes one request to
# completion before it moves on to the next request.  This is usually OK when
# testing, but it is not OK in production.  Your assignment is to make this
# server use non-blocking IO.

# This server is also synchronous, which means that it only starts sending a
# response after it has the entire contents of the file.  This is usually OK
# when testing, but it is not OK in production.  Your assignment is to make
# this server use sendfile to avoid reading the entire file into memory.

# This server also does not close connections properly
