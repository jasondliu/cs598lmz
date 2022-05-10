import socket
import sys
import time
import threading
import Queue
import os
import signal
import errno

# Global variables
#
# The following variables are used to control the operation of the
# proxy:
#
# listen_port - the port number on which the proxy server listens for
# incoming connections.  You can run the proxy server and client on
# the same machine for testing purposes, in which case this should
# be set to 0, which will cause the proxy server to listen on a
# randomly allocated port number.
#
# www_host - the host name or IP address of the server that the proxy
# server will connect to and issue HTTP requests on behalf of the
# client.  This can be set to "www.cs.unc.edu", for example, if you
# are testing your code on the departmental web server.
#
# www_port - the port number of the server that the proxy server will
# connect to and issue HTTP requests on behalf of the client.  This
# should almost always be set to 80, which is the standard port for
# HTTP connections.
#
# cache_size - the
