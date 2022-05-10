import mmap
import os
import re
import shutil
import subprocess

import six
from six.moves import input

from . import appdirs
from .exception import CliException, CliApplicationException
from .exception import CliNetworkException, CliUploadException
from .exception import CliDownloadException
from .exception import CliFileException, CliServerException

from .utils import (
    detect_http_proxy,
    detect_https_proxy,
    get_output,
    get_output_json,
    retry,
    retry_on_error,
    retry_on_conn_error,
    run_command,
    truncate_str,
)

from .utils_file import (
    calculate_md5_sum,
    calculate_sha256_sum,
    check_md5_sum,
    check_sha256_sum,
    compress_file,
    decompress_file,
    find_in_path,
    get_file_name,
    is_file_writable,
    is_regular_file
