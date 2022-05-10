import mmap
import os
import re
import sys

from collections import defaultdict
from collections import OrderedDict
from itertools import groupby
from operator import itemgetter

import numpy as np
import pandas as pd

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC

from Bio.SeqUtils import GC

from Bio.SeqUtils.ProtParam import ProteinAnalysis

from Bio.SeqUtils.MeltingTemp import Tm_staluc

from Bio.SeqUtils.CheckSum import seguid

from Bio.SeqUtils.lcc import lcc_simp

from Bio.SeqUtils.CodonUsage import CodonAdaptationIndex

from Bio.SeqUtils.CodonUsage import CodonUsageTable

from Bio.SeqUtils.CodonUsage import SynonymousCodons

from Bio.SeqUtils.CodonUsage import CodonUsage

from Bio.SeqUtils.MeltingTemp
