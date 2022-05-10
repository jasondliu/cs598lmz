import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
 
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#pylint: disable-msg=
"""
File       : DD.py
Author     : Valentin Kuznetsov <vkuznet AT gmail dot com>
Description: 
"""

# system modules
import os
import re
import sys
import time
import random
import types
import urllib
import httplib
import optparse

# package modules
from DCAF.utils.utils import getdata, get_key_cert, genkey
from DCAF.utils.utils import timestamper, timeout_manager
from DCAF.utils.utils import parse_data, parse_proxy, parse_data_json
from DCAF.utils.utils import get_proxy_info, get_data_and_cert, get_data_and_key_cert
from DCAF.utils.utils import parse_data_xml, get_data_and_key_cert_json, get_data_and_key_cert_xml
from DCAF.utils.utils import parse_data_
