import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess
import re
import json
import hashlib
import base64
import urllib
import urllib2
import socket
import platform
import Queue

try:
    import gnomekeyring
    import gnomekeyring as gkey
except:
    pass

try:
    import win32crypt
except:
    pass

try:
    import keyring
except:
    pass

try:
    from Crypto.Cipher import AES
except:
    pass

try:
    import gnomekeyring
    import gnomekeyring as gkey
except:
    pass

# Global Variables

#Global Variables

# These are the urls for the different tlds
# The urls are only for the main page, for the signin
# page you need to add /signin
# a list of all the tlds can be found here
# http://en.wikipedia.org/wiki/List_of_Internet_top-level_domains

# The list of urls can be updated with any
