import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def parse_args():
    parser = argparse.ArgumentParser(description='Create a dictionary from a given file')
    parser.add_argument('--input', type=str, required=True, help='Path to the file to be read')
    parser.add_argument('--output', type=str, required=True, help='Path to the output file')
    parser.add_argument('--encoding', type=str, default='utf8', help='Encoding of the input file')
    parser.add_argument('--min_frequency', type=int, default=0, help='Minimum frequency of a word to be included into the dictionary')
    parser.add_argument('--max_words', type=int, default=0, help='Maximum number of words to be included into the dictionary')
    return parser.parse_args()

def main():
    args = parse_args()
    freq_dict = {}
    with open(args.input, 'rb') as input_file:
        for line in input_file:

