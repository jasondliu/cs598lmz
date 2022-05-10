import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util

class Client(object):
    """
    Client object.
    """

    def __init__(self, host, port, username, password, use_tls=False,
                 tls_verify=True, tls_ca_certs=None, tls_certfile=None,
                 tls_keyfile=None, tls_ciphers=None, tls_protocol=None,
                 tls_version=None, tls_cert_reqs=None, tls_sni_hostname=None,
                 tls_suppress_ragged_eofs=None, tls_cafile=None,
                 tls_capath=None, tls_crlfile=None, tls_dhfile=None,
                 tls_eccertfile=None, tls_eckeyfile=None,
                 tls_key_password=None, tls_server_hostname=None,
                 tls_session_
