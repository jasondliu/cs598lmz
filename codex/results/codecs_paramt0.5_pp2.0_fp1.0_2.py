import codecs
codecs.register_error('backslashreplace', codecs.backslashreplace_errors)

from . import common

from .common import (
    _validate_path,
    _validate_file,
    _validate_output_path,
    _validate_output_file,
    _validate_output_dir,
    _validate_output_dir_exists,
    _validate_output_file_exists,
    _validate_output_file_not_exists,
)

from .common import (
    _get_input_dir,
    _get_output_dir,
    _get_data_dir,
    _get_log_dir,
    _get_cache_dir,
    _get_config_dir,
    _get_config_file,
)

from .common import (
    _get_input_file,
    _get_output_file,
    _get_data_file,
    _get_log_file,
    _get_cache_file,
)

from .common import (
    _get_
