import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Simple class for holding a genome
class Genome:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def __repr__(self):
        return '>{}\n{}'.format(self.name, self.sequence)

# Class for comparing 2 input genomes
class CompareGenomes:
    def __init__(self, genome1, genome2):
        self.genome1 = genome1
        self.genome2 = genome2

    # Method for running global alignments
    def global_align(self):
        # Initialize variables
        seq1 = self.genome1.sequence
        seq2 = self.genome2.sequence
        len1 = len(seq1)
        len2 = len(seq2)
        score = 0
        align1 = ''
        align2 = ''

        # Initialize dynamic programming matrix
