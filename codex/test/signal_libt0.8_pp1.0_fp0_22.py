import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

import os
from multiprocessing import Pool, Process, Queue
from itertools import repeat

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd
import numpy as np

from scripts.align import align_seqs
from scripts.align import count_char_in_alignment
from scripts.align import consensus_in_region
from scripts.align import reformat_alignment_header
from scripts.align import extract_fasta_from_alignment
from scripts.align import sample_alignment_from_file
from scripts.sequence import get_non_redundant_from_alignment
from scripts.sequence import initialize_dist_matrix
from scripts.sequence import get_n_highest_frequency_from_alignment
from scripts.sequence import fasta_to_consensus_seq_by_frequency

from scripts.alignment_refinement import filter_alignment_based_on_information_content

