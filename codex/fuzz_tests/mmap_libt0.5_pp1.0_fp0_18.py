import mmap
from pathlib import Path
from functools import wraps

from . import utils

from .utils import (
    _get_default_path,
    _get_default_dir,
    _get_default_filename,
    _get_default_filepath,
    _get_file_path,
    _get_file_dir,
    _get_file_name,
    _get_file_extension,
    _get_file_path_no_extension,
    _get_file_path_from_name,
    _get_file_path_from_name_or_path,
    _get_file_name_from_path,
    _get_file_extension_from_path,
    _get_file_path_no_extension_from_path,
    _get_file_path_from_path,
    _get_file_dir_from_path,
    _get_file_path_from_path_or_name,
    _get_file_name_from_path_or_name,
    _get_
