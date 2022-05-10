import mmap
from collections import defaultdict
from itertools import combinations, product
from math import sqrt

from tqdm import tqdm

from .utils import read_pairs
from .utils import read_fasta
from .utils import read_fastq
from .utils import read_fasta_dict
from .utils import read_fastq_dict
from .utils import read_fasta_dict_simple
from .utils import read_fastq_dict_simple
from .utils import read_bam
from .utils import read_bam_to_dict
from .utils import read_bam_to_dict_simple
from .utils import read_bam_to_dict_simple_sorted
from .utils import read_bam_to_dict_simple_sorted_contigs
from .utils import read_bam_to_dict_simple_sorted_contigs_intervals
from .utils import read_bam_to_dict_simple_sorted_contigs_intervals_stranded
from .utils import read_bam_to_dict_simple_sorted_contigs
