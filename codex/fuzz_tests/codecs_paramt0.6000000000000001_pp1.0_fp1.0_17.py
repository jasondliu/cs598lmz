import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Parse the input file.')
    parser.add_argument('--input', '-i', type=str, required=True,
                        help='The input file.')
    parser.add_argument('--output', '-o', type=str, required=True,
                        help='The output file.')
    args = parser.parse_args()

    with codecs.open(args.input, 'r', 'utf-8', 'strict') as fin, \
         codecs.open(args.output, 'w', 'utf-8') as fout:
        for line in fin:
            line = line.strip()
            if not line: continue
            fout.write(line + '\n')

if __name__ == '__main__':
    main()
