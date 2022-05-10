import mmap
import gzip
import pandas as pd

import os
import re
import sys
import struct
import glob
import codecs
import tempfile
import subprocess
import itertools

from collections import defaultdict
from multiprocessing import Pool as ThreadPool, Queue, Value, Process
from multiprocessing import cpu_count
from functools import partial
from time import time
from optparse import OptionParser

from python_modules.utils.IdMapper import IdMapper, IdMapperException

from python_modules.file_formats.gff import GFFParser
from python_modules.correspondence_detection.detect_correspondence_between_annotations import detect_correspondence_between_annotations, detect_correspondence_between_annotations_using_blast_threaded
from python_modules.file_formats.bed import BEDParser, BEDWriter
from python_modules.utils.sequence_retrieval import retrieve_sequences_from_fasta
from python_modules.utils.sequence_retrieval import retrieve_sequences_from_fast
