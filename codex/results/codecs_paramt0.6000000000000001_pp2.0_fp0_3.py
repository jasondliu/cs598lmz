import codecs
codecs.register_error('surrogate_or_special',
                      lambda e: (u'', e.start + 1))

def main(args):
    for line in args.input:
        try:
            sys.stdout.write(line.decode('utf-8'))
        except UnicodeDecodeError:
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove non-UTF8 characters from input')
    parser.add_argument('input', metavar='FILE', type=argparse.FileType('r'),
                        nargs='?', default=sys.stdin,
                        help='input file (defaults to stdin)')
    args = parser.parse_args()
    main(args)
