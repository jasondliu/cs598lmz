import mmap
import sys
from typing import List
import random

import sbd

arg_parse = argparse.ArgumentParser(description='Toy sentence segmentor that is useful for making training data')
arg_parse.add_argument('text_file', type=str, help='input text')
arg_parse.add_argument('output_file', type=str, help='output file')
arg_parse.add_argument('--window-size', type=int, default=256, help='size of context window for each sentence (default: 256)')

if __name__ == '__main__':
    args = arg_parse.parse_args()

    with open(args.text_file, 'r', encoding='utf-8-sig') as fp:
        input_text = mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ)

        segmentor = sbd.SentenceSegmentor('braille_sentence_segmentor')

        # Segment the text into sentences
