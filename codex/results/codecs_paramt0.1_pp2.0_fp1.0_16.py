import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Convert a file to a different encoding')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-f', '--from', help='Input encoding', required=True)
    parser.add_argument('-t', '--to', help='Output encoding', required=True)
    args = parser.parse_args()

    with codecs.open(args.input, 'r', args.from, 'strict') as f:
        with codecs.open(args.output, 'w', args.to, 'strict') as o:
            o.write(f.read())

if __name__ == '__main__':
    main()
