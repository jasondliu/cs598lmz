import mmap
import math
import os
import platform
import re
import subprocess
import sys
import time

from os.path import expanduser

# This was copied from lib/module_utils/urls.py in Ansible.
# This only handles http/https schemes.
def open_url(url, headers=None, validate_certs=True):
    '''
    Open a URL for reading.

    :arg url: A string containing a URI
    :kwarg headers: A dictionary of HTTP headers to send with the
        :class:`Request <request:Request>`.
    :kwarg validate_certs: Whether or not to validate HTTPS certificates.
        Defaults to True.
    :returns: a :class:`Response <request:Response>` object
    '''
    # validate_certs = validate_certs and boto.config.getbool('Boto', 'ValidateCertificate', True)
    validate_certs = validate_certs and True

    request_func = requests.get
