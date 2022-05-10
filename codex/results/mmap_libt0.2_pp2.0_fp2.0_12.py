import mmap
import sys
import os
import re
import time
import subprocess
import shutil
import glob
import struct
import array
import math
import random
import itertools
import operator
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from optparse import OptionParser
from optparse import OptionGroup
from operator import itemgetter
from operator import attrgetter
from operator import methodcaller
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from Bio.SeqIO.QualityIO import FastqPhredIterator
from Bio.SeqIO.QualityIO import FastqPhredWriter
from Bio.SeqIO.QualityIO import FastqSangerIterator
from Bio.SeqIO.QualityIO import FastqSolexaIterator
from Bio.SeqIO.QualityIO import FastqIlluminaIterator
from Bio.SeqIO.QualityIO import FastqPhredQualityWriter
from Bio.Seq
