import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

import common
import edify_generator

OPTIONS = common.OPTIONS
OPTIONS.info_dict = None
OPTIONS.input_tmp = None
OPTIONS.output_zip = None
OPTIONS.script = None
OPTIONS.two_step = False
OPTIONS.updater_binary = None
OPTIONS.extracted_input = None
OPTIONS.target_info_dict = None
OPTIONS.source_info_dict = None
OPTIONS.target_files_info = None
OPTIONS.source_tmp = None
OPTIONS.target_tmp = None
OPTIONS.source_file = None
OPTIONS.target_file = None
OPTIONS.verify = False
OPTIONS.verify_property = None
OPTIONS.verify_value = None
OPTIONS.require_verify_zip = False
OPTIONS.oem_dict = None
OPTIONS.oem
