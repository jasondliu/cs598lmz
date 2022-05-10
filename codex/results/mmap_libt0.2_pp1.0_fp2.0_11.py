import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

import common
import edify_generator

OPTIONS = common.OPTIONS
OPTIONS.info_dict = None
OPTIONS.input_tmp = None
OPTIONS.output_zip = None
OPTIONS.script = None
OPTIONS.two_step = False
OPTIONS.updater_binary = None
OPTIONS.verify = False
OPTIONS.verify_property = None
OPTIONS.verify_value = None
OPTIONS.wipe_user_data = False

def main(argv):
  def option_handler(o, a):
    if o in ("-a", "--add_files"):
      OPTIONS.add_files.append(a)
    elif o in ("-e", "--delete_files"):
      OPTIONS.delete_files.append(a)
    elif o == "--board_config":
      OPTIONS.info_dict = common.
