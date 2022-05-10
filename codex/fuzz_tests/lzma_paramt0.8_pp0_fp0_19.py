from lzma import LZMADecompressor
LZMADecompressor.__module__ = "lzma"

import argparse
import base64
import codecs
import contextlib
import json
import os
import sys
import tempfile
import zipfile

from . import DEFAULT_PYTHON_VERSION, DEFAULT_TARGET, REQUIRED_HOSTS, SUPPORTED_PLATFORMS, SUPPORTED_PYTHON_VERSIONS

parser = argparse.ArgumentParser(prog="fbs freeze")
parser.add_argument(
    '-p', '--project-dir',
    help='Build from the given project directory',
    default='.'
)
parser.add_argument(
    '--out', '--output-dir', '-o',
    help='Place output in the given directory',
    default='target'
)
parser.add_argument(
    '--version',
    help='Version to build. Default is to read the version from the given project'
)
parser.add_argument(
    '--app',
    help='Application to build. Default is to build every application'
)
parser.add
