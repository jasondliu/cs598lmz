import mmap
import gzip
from collections import defaultdict
import pandas as pd
from pprint import pprint
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
import os
import re

from toolz.curried import keyfilter, valfilter, pipe, get
from toolz.itertoolz import groupby
from cytoolz.curried import first, second, nth, map, filter, reduce, concat

from Bio.SeqFeature import FeatureLocation, CompoundLocation
from Bio.SeqFeature import SeqFeature
from Bio.SeqFeature import Reference
from Bio.SeqFeature import ExactPosition
from Bio.SeqFeature import AfterPosition
from Bio.SeqFeature import BeforePosition

from Bio.SeqFeature import FeatureLocation
from Bio.SeqFeature import SeqFeature
from Bio.SeqFeature import Reference
from Bio.SeqFeature import ExactPosition
from Bio.SeqFeature import AfterPosition
from Bio.SeqFeature import BeforePosition

from Bio.Se
