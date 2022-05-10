import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import shutil
import itertools
import argparse
import textwrap
import subprocess
import multiprocessing

import numpy as np

import jinja2

from . import __version__
from . import __author__
from . import __email__
from . import __license__

from . import util
from . import logger
from . import genome
from . import annotation
from . import psl
from . import gtf
from . import fasta
from . import fastq
from . import sam
from . import bam
from . import bamqc
from . import bamstats
from . import bam2bw
from . import bam2wig
from . import bam2bedgraph
from . import bam2bed
from . import bam2fastq
from . import bam2fasta
from . import bam2count
from . import bam2tag
from . import bam2cov
from . import bam2depth
from . import bam2clip

