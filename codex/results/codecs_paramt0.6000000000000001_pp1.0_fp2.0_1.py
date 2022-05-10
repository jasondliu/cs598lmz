import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--file', help='file to process', required=True)
parser.add_argument('-o', '--output', help='output file')
parser.add_argument('-d', '--delimiter', help='delimiter to use', default='\t')
parser.add_argument('-c', '--column', help='column to process', type=int, default=0)
args = parser.parse_args()

if args.output is None:
    args.output = os.path.splitext(args.file)[0] + '_parsed' + os.path.splitext(args.file)[1]

with codecs.open(args.file, encoding='utf-8', errors='replace_with_space') as csvfile:
    reader = csv.reader(csvfile, delimiter=args.delimiter)

