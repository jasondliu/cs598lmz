import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

from . import util

# -----------------------------------------------------------------------------

# The name of the file that contains the list of files to be included in the
# archive.
ARCHIVE_LIST_FILENAME = 'archive_list.txt'

# The name of the file that contains the list of files to be excluded from the
# archive.
EXCLUDE_LIST_FILENAME = 'exclude_list.txt'

# The name of the file that contains the list of files to be included in the
# archive.
FILE_LIST_FILENAME = 'file_list.txt'

# The name of the file that contains the list of files to be included in the
# archive.
INCLUDE_LIST_FILENAME = 'include_list.txt'

# The name of the file that contains the list of files to be included in the
# archive.
MANIFEST_FILENAME = 'manifest.txt'

# The name of the file that contains the list of files
