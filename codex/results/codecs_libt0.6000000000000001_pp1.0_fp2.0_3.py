import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.SeqFeature import FeatureLocation, SeqFeature
from collections import defaultdict
from collections import Counter
import re
from Bio import Entrez
Entrez.email = "matthew.kling@gmail.com"
import time
import os
from Bio.PDB import PDBParser, PPBuilder
from Bio.PDB.Residue import Residue

import sys
sys.path.insert(0, '../')
from py_scripts.helpers import *
from py_scripts.hiv_helpers import *
from py_scripts.mutation_helpers import *
from py_scripts.plot_helpers import *
from py_scripts.sim_helpers import *
from py_scripts.tree_helpers import *
from py_scripts.mutation_models import *
from py_scripts
