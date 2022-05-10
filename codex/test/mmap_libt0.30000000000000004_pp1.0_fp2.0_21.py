import mmap
import os
import re
import sys
import time

from collections import defaultdict
from collections import namedtuple
from contextlib import closing
from datetime import datetime
from itertools import chain
from itertools import groupby
