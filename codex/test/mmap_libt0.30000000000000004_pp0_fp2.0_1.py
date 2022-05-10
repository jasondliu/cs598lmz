import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile

# TODO(josh): Make this a command line option
# This is the directory where the build is taking place.
# It is used to find the build_id file.
# It is also used to find the build_id file in the case of a
# cross-architecture build.
BUILD_DIR = 'out/Release'

# TODO(josh): Make this a command line option
# This is the directory where the build is taking place.
# It is used to find the build_id file.
# It is also used to find the build_id file in the case of a
# cross-architecture build.
BUILD_DIR_DEBUG = 'out/Debug'

# TODO(josh): Make this a command line option
# This is the directory where the build is taking place.
# It is used to find the build_id file.
# It is also used to find the build_id file in the case of a
# cross-architecture build.
