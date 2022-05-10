import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import struct
import time
import datetime

# Define some contants
#
# See http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html for descriptions
#
class HTTPMethod:
    GET     = 1
    HEAD    = 2
    POST    = 3
    PUT     = 4
    DELETE  = 5
    TRACE   = 6
    OPTIONS = 7
    CONNECT = 8
    PATCH   = 9

class HTTPVersion:
    HTTP09 = 0
    HTTP10 = 1
    HTTP11 = 2
    HTTP20 = 3

class HTTPResponseCode:
    Continue                     = 100
    SwitchingProtocols           = 101
    Processing                   = 102
    OK                           = 200
    Created                      = 201
    Accepted                     = 202
    NonAuthoritativeInformation  = 203
    NoContent                    = 204
    ResetContent                 = 205
    PartialContent               = 206
    MultiStatus                  = 207
    AlreadyReported              = 208

