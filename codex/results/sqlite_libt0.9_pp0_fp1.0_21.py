import ctypes
import ctypes.util
import threading
import sqlite3
import kerberos
from k5test_services.gss_acl import *
from k5test_services.kerberos import ServiceWrapper, service_names, service_ips
import random
import ipaddress
import json
from k5test_services.service_common import service_cleanup, \
    service_run_all, service_setup_all, service_teardown, SRX
import k5test_services.service_common as common
import time
from k5test_services.service_common import *


def get_gss_name(spn, service_name):
    if spn.startswith('drill_init@'):
        hostname = spn[len('drill_init@'):]
        spn = ('drill/' + socket.gethostbyname(hostname))

    if spn == 'host@' + os.getenv('KRB5_CONFIG_REALM'):
        spn = 'host'

    if '\@' in spn:
        return gssapi.Name(spn, gss
