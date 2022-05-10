import codecs
codecs.register_error('strict', codecs.ignore_errors)

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input map file')
parser.add_argument('--output', help='output map file')
args = parser.parse_args()

output = open(args.output, 'w')

with codecs.open(args.input, 'r', 'utf-8', 'ignore') as input:
    for line in input:
        line = line.strip()
        if line.startswith('R ') or line.startswith('R='):
            fields = line.split(' ')
            if len(fields) == 2:
                line = 'R' + fields[1]
        output.write(line + '\n')
