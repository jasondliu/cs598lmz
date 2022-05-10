import mmap
import os
import sys
import logging
import time
import struct
import random
import string
import socket

logger = logging.getLogger(__name__)

# This is the size of a single page in the shared memory
# It is used to calculate the offset of the page to be read
PAGE_SIZE = 4096

# This is the size of the header in the shared memory
# It is used to calculate the offset of the page to be read
HEADER_SIZE = 5

# This is the size of the footer in the shared memory
# It is used to calculate the offset of the page to be read
FOOTER_SIZE = 5

# This is the size of the page in the shared memory
# It is used to calculate the offset of the page to be read
PAGE_DATA_SIZE = PAGE_SIZE - (HEADER_SIZE + FOOTER_SIZE)

# This is the size of the page in the shared memory
# It is used to calculate the offset of the page to be read
