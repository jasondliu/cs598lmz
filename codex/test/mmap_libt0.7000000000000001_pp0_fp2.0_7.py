import mmap
import re
import random
import argparse

alphabet = "abcdefghijklmnopqrstuvwxyz"

def main(args):
    for filename in os.listdir(args.data_dir):
        if filename.endswith("_token.txt"):
            input_filename = os.path.join(args.data_dir, filename)
            output_filename = os.path.join(args.data_dir, filename.replace("_token.txt", "_punc.txt"))
            with open(input_filename, "r") as input_file:
                with open(output_filename, "w") as output_file:
                    for line in input_file:
                        if args.prob_punctuation > 0:
                            line = add_punctuation(line, args.prob_punctuation)
                        if args.prob_space <= 1:
                            line = remove_spaces(line, args.prob_space)
                        output_file.write(line)

