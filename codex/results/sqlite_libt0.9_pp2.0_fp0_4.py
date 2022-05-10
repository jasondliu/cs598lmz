import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import io
import requests

import pyasn

class ACL(object):
    def __init__(self, dbpath):
        self.db = sqlite3.connect(dbpath)
        self.cur = self.db.cursor()

    def is_allowed(self, ip, port):
        self.cur.execute('SELECT '+
                'acl_allow_invalid_pkts, '+
                'acl_allow_no_resolver_for_outbound, '+
                'acl_allow_whitelisted, '+
                'acl_restrict_subnets, '+
                'acl_whitelist_subnets, '+
                'acl_restrict_ports, '+
                'acl_whitelist_ports, '+
                'acl_restrict_ports_outbound, '+
                'acl_whitelist_ports_outbound, '+
                'acl_restrict_ports_inbound, '+
                'acl_whitelist_ports_inbound, '

