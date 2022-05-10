import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input file')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-l', '--lang', help='Language')
    args = parser.parse_args()

    if not args.input or not args.output or not args.lang:
        parser.print_help()
        sys.exit(1)

    with codecs.open(args.input, 'r', 'utf-8') as f:
        data = f.read()

    with codecs.open(args.output, 'w', 'utf-8') as f:
        f.write(convert(data, args.lang))

def convert(data, lang):
    data = data.replace('\r\n', '\n')
    data = data.replace('\r', '\n')

    lines = data.split('\n')

    if lang ==
