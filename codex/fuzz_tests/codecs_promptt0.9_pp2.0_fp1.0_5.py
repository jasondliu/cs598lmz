import codecs
# Test codecs.register_error(‘strict’, codecs.strict_errors) - Python 2/3 compatibility
import json
import logging
import os
import subprocess
import sys
import tempfile
import time

from js_host import JSState

XML_PROLOG = '<?xml version="1.0" encoding="utf-8"?>\n'
RDFAJS_TAG = '<script class="rdfajs-script" type="application/javascript; version=1.1">\n'

CUR_DIR = os.path.split(__file__)[0]
SERVER_ROOT = os.path.abspath(os.path.join(CUR_DIR, '..', '..', 'bin', 'server'))
DATA_DIR = os.path.join(CUR_DIR, 'data')
EXAMPLE_RDF_DIR = os.path.join(CUR_DIR, 'example-rdf-files')

# ------------------------------------------------------------------------------

def read_example_data_file(name):
    """Open and read contents of file, returning contents as Unicode."""
