import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Convert a file to a different encoding')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-e', '--encoding', help='Encoding', required=True)
    args = parser.parse_args()

    with codecs.open(args.input, 'r', 'strict') as f:
        with codecs.open(args.output, 'w', args.encoding) as o:
            for line in f:
                o.write(line)

if __name__ == '__main__':
    main()
