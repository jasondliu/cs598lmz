import mmap
import sys
import os
import re
import datetime
import math
import getopt
import glob
import shutil
from collections import defaultdict
from collections import namedtuple

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna, generic_protein

from Bio.SeqUtils import GC

from Bio.Alphabet import IUPAC,Gapped
from Bio.Seq import MutableSeq
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO
from Bio.Alphabet import IUPAC,Gapped
from Bio.Seq import MutableSeq
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo import BaseTree
from Bio.Align import MultipleSeqAlignment
from Bio import Al
