import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import socket
import time
import re
import os
import json
import random
import util

def get_proxy_list():
    """
    Get a list of proxies

    Returns:
        [{'ip':'', 'port':'', 'protocol':'socks4/socks5/http', 'anonymity':'anonymous/elite'}, ...]
    """
    # http://www.us-proxy.org/
    # http://www.socks-proxy.net/
    # http://www.xroxy.com/proxylist.php
    # http://www.samair.ru/proxy/time-01.htm
    # http://www.gatherproxy.com/
    # http://www.proxylists.net/
    # http://www.proxz.com/proxy_list_high_anonymous_0.html
    # http://www.proxz.com/proxy_list_anonymous_0.html
    # http://www.proxz.com/proxy_list_transparent_0.html

