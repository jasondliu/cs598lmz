import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from datetime import timedelta
from itertools import chain
from itertools import groupby
from itertools import islice
from itertools import tee
from operator import itemgetter
from operator import methodcaller
from optparse import OptionParser
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT

# TODO:
# - Add support for multiple input files
# - Add support for multiple output files
# - Add support for multiple input/output files
# - Add support for multiple input/output files with different formats
# - Add support for multiple input/output files with different formats and
#   different time ranges
# - Add support for multiple input/output files with different formats and
#   different time ranges and different time resolutions
# - Add support for multiple input/output files with different formats and
#   different time ranges and different time resolutions and different
#   timezones
# - Add support for multiple input/output files with different formats and
#   different time
