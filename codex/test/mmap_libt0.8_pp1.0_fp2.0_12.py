import mmap
import os
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--m", dest="m", help="run on mpi file")
parser.add_option("--o", dest="o", help="output file")
parser.add_option("--l", dest="l", help="log file")
(options, args) = parser.parse_args()

if not options.m and not options.o and not options.l:
	print("You have to provide args!")
	exit()

log_file = open(options.l, "w")

mem_map = mmap.mmap(os.open(options.m, os.O_RDONLY), 0, prot=mmap.PROT_READ)

num_nodes = -1
num_edges = -1
num_iterations = -1

num_visited_nodes = 0
num_visited_edges = 0

f = open(options.o, 'w')

