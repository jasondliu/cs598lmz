import codecs
codecs.register_error("strict", codecs.ignore_errors)
#
import sys
import os
import appdirs
#
from . import version
#
# Set a default value for the user directory
#
user_dir = appdirs.user_data_dir(version.__appname__, version.__author__)
if not os.path.exists(user_dir):
    os.makedirs(user_dir)
#
# This is a hack to make the import of the user settings work
#
sys.path.append(user_dir)
#
# Import the user settings
#
from user_settings import *

#
# Set the system name and the user name
#
system_name = os.uname()[1]
user_name = os.environ["USER"]
#
# Set up the default values for the user settings
#
default_user_settings = {
    "debug_mode": False,
    "verbose_mode": False,
    "log_file": os.path.join(user_dir, "phynx.log"),
    "remote
