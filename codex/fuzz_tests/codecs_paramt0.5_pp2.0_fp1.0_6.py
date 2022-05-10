import codecs
codecs.register_error('strict', codecs.ignore_errors)

def parse_args():
    parser = argparse.ArgumentParser(description='Convert a set of input files to a single output file')
    parser.add_argument('--input_files', nargs='+', help='List of input files')
    parser.add_argument('--output_file', help='Output file')
    parser.add_argument('--encoding', default='utf8', help='Input file encoding')
    return parser.parse_args()

def main():
    args = parse_args()

    with codecs.open(args.output_file, 'w', args.encoding) as fout:
        for input_file in args.input_files:
            with codecs.open(input_file, 'r', args.encoding, errors='strict') as fin:
                fout.write(fin.read())

if __name__ == '__main__':
    main()
