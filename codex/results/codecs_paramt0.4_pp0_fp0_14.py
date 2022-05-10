import codecs
codecs.register_error("strict", codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Convert a text file to a sequence of words.')
    parser.add_argument('input', help='input file')
    parser.add_argument('output', help='output file')
    parser.add_argument('--encoding', default='utf-8', help='input file encoding')
    parser.add_argument('--lower', action='store_true', help='lowercase all words')
    parser.add_argument('--normalize', action='store_true', help='normalize punctuation')
    args = parser.parse_args()

    with codecs.open(args.input, 'r', args.encoding, 'strict') as f:
        with codecs.open(args.output, 'w', args.encoding, 'strict') as out:
            for line in f:
                if args.normalize:
                    line = normalize_punctuation(line)
                if args.lower:
                    line = line.lower()
                out.write
