import codecs
codecs.register_error('strict', codecs.ignore_errors)

parser = argparse.ArgumentParser(description='Create a file of strings to choose from for a string in the question')
parser.add_argument('-i', '--input',
                    help='input file (must be tab-delimited)',
                    default=None)
args = parser.parse_args()

if args.input is None:
    print('input file is required')
    quit()

infile = codecs.open(args.input, 'r', 'utf8')

line = infile.readline()
line = line.strip()
if len(line) > 0 and not line.startswith('#'):
    header = line.split('\t')
else:
    header = None

kv = {}

for line in infile:
    line = line.strip()
    if len(line) == 0:
        continue
    if line.startswith('#'):
        continue

    fields = line.split('\t')
    if header is None:
        header = fields

