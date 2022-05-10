from bz2 import BZ2Decompressor
BZ2Decompressor.extra_init_args = []
from bz2 import decompress
from urllib.request import urlopen
from urllib.error import URLError
from os import remove, rename, listdir, path
from re import compile, search
from shutil import move
from sys import argv

from lib.lib_print import log_info, log_warn, log_err
from lib.lib_print import log_progress, log_title, log_section
from lib.lib_print import log_progress_done, log_progress_start
from lib.lib_print import log_progress_continue, log_progress_stop
from lib.lib_print import log_info_h1, log_info_h2
from lib.lib_print import log_info_cont, log_info_cont_nl
from lib.lib_print import log_info_cont_nl_2
from lib.lib_print import log_info_cont_nl_3
from lib.lib_print import log_info_cont_nl_4
from lib.lib_print import log_info_cont_nl_5
