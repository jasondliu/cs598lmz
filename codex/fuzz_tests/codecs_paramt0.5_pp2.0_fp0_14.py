import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-file', help='path to input file', required=True)
parser.add_argument('-o', '--output-file', help='path to output file', required=True)
parser.add_argument('-d', '--delimiter', help='delimiter to use in output file', default='\t')
parser.add_argument('-f', '--field', help='field number to process', type=int, default=0)
parser.add_argument('-c', '--chars', help='number of characters to remove from the beginning of the field', type=int, default=0)
parser.add_argument('-a', '--append', help='append to output file', action='store_true')
parser.add_argument('-e', '--encoding', help='encoding of input file', default='utf-8')
parser.add_argument('-t', '--transliterate', help='transliterate output
