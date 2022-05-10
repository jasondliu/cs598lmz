import mmap
import glob
import os
from os import listdir
from os.path import isfile, join
import sys
import shutil
import subprocess
import gzip
import random

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC

def read_fasta(fp):
	name, seq = None, []
	for line in fp:
		line = line.rstrip()
		if line.startswith(">"):
			if name: yield (name, ''.join(seq))
			name, seq = line, []
		else:
			seq.append(line)
	if name: yield (name, ''.join(seq))

def read_fasta_dict(file):
	""" Reads a fasta file and returns a dictionary with the contigs/scaffolds 
	as keys
