import mmap,sys
import random

def read_fasta(filename):
	'''
	Read a fasta file and return a dictionary of sequences.
	'''
	f = open(filename, 'r')
	lines = f.readlines()

	seq = {}
	name = None
	for line in lines:
		if line[0] == '>':
			name = line[1:].strip()
			seq[name] = ''
		else:
			seq[name] += line.strip()

	return seq

def get_random_seq(seq, length):
	start = random.randint(0, len(seq) - length)
	stop = start + length
	return seq[start:stop]

def main(args):
	seq = read_fasta(args.input)[args.chrom]
	n_seqs = int(args.n)
	length = int(args.length)
	if args.length == 'chrom':
		length = len(seq)
	for i in range(n_seqs
