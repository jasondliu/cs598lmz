import codecs
codecs.register_error('strict', codecs.ignore_errors)

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
parser.add_argument('output_file', type=str)
args = parser.parse_args()

with codecs.open(args.input_file, 'r', 'utf-8') as f:
    with codecs.open(args.output_file, 'w', 'utf-8') as g:
        for line in f:
            line = line.strip()
            if line == '<s>':
                continue
            print >>g, line
