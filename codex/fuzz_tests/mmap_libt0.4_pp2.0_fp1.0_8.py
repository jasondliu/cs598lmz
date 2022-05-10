import mmap
import os
import re
import sys
import time
import traceback

#------------------------------------------------------------------------------
# Global constants.
#------------------------------------------------------------------------------

# The name of the file that contains the list of files to be processed.
LIST_FILE_NAME = 'list.txt'

# The name of the file that contains the list of files to be excluded.
EXCLUDE_FILE_NAME = 'exclude.txt'

# The name of the file that contains the list of files to be included.
INCLUDE_FILE_NAME = 'include.txt'

# The name of the file that contains the list of files to be deleted.
DELETE_FILE_NAME = 'delete.txt'

# The name of the file that contains the list of files to be renamed.
RENAME_FILE_NAME = 'rename.txt'

# The name of the file that contains the list of files to be copied.
COPY_FILE_NAME = 'copy.txt'

# The name of the file that contains the list of files to be moved.
MOVE_FILE_NAME = 'move.txt'
