import select
# Test select.select
# Use select function to create an I/O multiplexing
# Input is standard input, output is standard output,
# the other two is standard network port 80
import sys,time
inputs = [sys.stdin]
outputs = [sys.stdout]
exceptional = []

