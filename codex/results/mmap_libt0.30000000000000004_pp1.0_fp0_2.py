import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from optparse import OptionParser
from subprocess import Popen, PIPE

from pysam import Samfile
from pybedtools import BedTool

from bx.intervals.intersection import Interval, IntervalTree
from bx.intervals.intersection import IntervalTreeNode
from bx.intervals.intersection import IntervalTreeIterator
from bx.intervals.intersection import IntervalTreeIteratorDepth

from bx.intervals.intersection import IntervalTreeNode
from bx.intervals.intersection import IntervalTreeIterator
from bx.intervals.intersection import IntervalTreeIteratorDepth

from bx.intervals.intersection import IntervalTreeNode
from bx.intervals.intersection import IntervalTreeIterator
from bx.intervals.intersection import IntervalTreeIteratorDepth

from bx.intervals.intersection import IntervalTreeNode
from bx.
