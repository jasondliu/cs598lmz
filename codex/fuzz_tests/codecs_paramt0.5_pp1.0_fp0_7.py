import codecs
codecs.register_error('strict', codecs.ignore_errors)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', required=True, help='input file')
    parser.add_argument('-o', '--output', dest='output', required=True, help='output file')
    return parser.parse_args()


def process_line(line):
    line = line.strip()
    if line == '':
        return None
    if line.startswith('#'):
        return None
    if '=' not in line:
        return None
    key, value = line.split('=', 1)
    key = key.strip()
    value = value.strip()
    try:
        value = unicode(value, 'utf-8')
    except UnicodeDecodeError:
        value = unicode(value, 'utf-8', 'strict')
    return key, value


def main():
    args = parse_args()
    with open(args.input, 'r')
