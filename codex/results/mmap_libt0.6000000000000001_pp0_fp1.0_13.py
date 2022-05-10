import mmap
import os
import re
import shutil
import subprocess
import tempfile
import warnings

from . import _common
from ._common import (
    GzippedFile,
    _get_config,
    _get_conda_root_prefix,
    _get_rc_urls,
    _get_python_version_for_prefix,
    _url_to_filename,
    _url_to_file_path,
    _get_python_version_for_prefix,
    _get_platform,
    _get_md5sum,
    _get_channel_urls,
    _replace_url_context,
    _ensure_subdir,
    _extract_tarball,
    _mkdir_p,
    _get_cache_directory,
    _get_download_cache_directory,
    _get_download_cache_short_path,
    _get_download_cache_long_path,
    _get_download_cache_short_prefix,
    _get_download_cache_long_prefix,
    _get_pkg
