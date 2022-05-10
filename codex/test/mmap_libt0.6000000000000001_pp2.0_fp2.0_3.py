import mmap
import re
import subprocess
import os

# Read in the file
f = open('/proc/meminfo', 'r')
