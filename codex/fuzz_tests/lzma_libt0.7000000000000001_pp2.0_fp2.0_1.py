import lzma
lzma.open
'''

import io
import os
import sys
import re
import gzip
import bz2
import lzma
import contextlib
import mmap
import unicodedata
import collections

class FileTypes:
    UNKNOWN = 0
    FASTA = 1
    FASTQ = 2
    SAM = 3
    BAM = 4
    VCF = 5
    BED = 6
    GTF = 7
    GFF = 8
    CSV = 9
    TAB = 10
    TXT = 11 
    XML = 12
    HTML = 13
    OTHER = 99

class FileReader:
    """
    Generic file reader.

    The FileReader class provides the ability to read and iterate over
    different types of files. This class should be used as a base class
    to provide more specific functionality.

    The FileReader class provides an iterator interface to the underlying
    file. In order to support different file types (e.g., FASTA, FASTQ,
    SAM, etc.), the iterator returns a string representing the next line
    of the file.
