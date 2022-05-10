import mmap
import sys
import subprocess
import shlex
import re


# Add support for "/C=US/ST=FL/O=MyOrg/CN=mydomain.com" in
# Makefile for local testing
BASEDIR = os.path.abspath(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '..'))
DEFAULT_SSL_DIR = os.path.join(BASEDIR, 'files/ssl')
DEFAULT_OPENSSL_CNF = os.path.join(DEFAULT_SSL_DIR, 'openssl.cnf')
