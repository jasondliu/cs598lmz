import mmap
import os
import re
import signal
import subprocess
import sys

from lib import get_build_dir, get_cache_dir, get_install_dir, get_source_dir
from lib import get_os_version, get_os_architecture, get_os_distribution
from lib import get_os_codename, get_os_release, get_os_system
from lib import get_os_machine, get_os_machine_bit, get_os_username
from lib import get_os_home_dir, get_os_home_drive, get_os_platform
from lib import get_os_processor, get_os_uname, get_os_file_system_encoding
from lib import get_os_default_encoding, get_os_default_error_encoding
from lib import get_os_default_environment_encoding, get_os_path_sep
from lib import get_os_path_altsep, get_os_path_extsep, get_os_path_devnull
from lib import get_os_path_join,
