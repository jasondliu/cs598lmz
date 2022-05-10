import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib
import urllib2
import urlparse
import zipfile

from distutils.version import LooseVersion

from utils import (
    check_output,
    download_file,
    extract_zip,
    get_file_hash,
    get_file_size,
    get_file_url,
    get_file_urls,
    get_file_urls_from_manifest,
    get_file_urls_from_manifest_v2,
    get_file_urls_from_manifest_v3,
    get_file_urls_from_manifest_v4,
    get_file_urls_from_manifest_v5,
    get_file_urls_from_manifest_v6,
    get_file_urls_from_manifest_v7,
    get_file_urls_from_manifest_v8,
    get_file_urls_from
