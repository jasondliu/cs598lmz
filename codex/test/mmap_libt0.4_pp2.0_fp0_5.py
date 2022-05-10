import mmap
import sys
import os
import os.path
import random
import json
import time
import math

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 {} <input_file> <output_file>".format(sys.argv[0]))
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print("Error: input file {} not found".format(input_file))
        sys.exit(1)

    if os.path.isfile(output_file):
        print("Warning: output file {} already exists".format(output_file))
        sys.exit(1)

    print("Input file: {}".format(input_file))
    print("Output file: {}".format(output_file))

