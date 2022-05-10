import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape)

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'surrogate_or_strict')
sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'surrogate_or_strict')


def main(args):
    """Main function."""
    if len(args) < 2:
        print('Usage: {} <file>'.format(args[0]), file=sys.stderr)
        sys.exit(1)

    # Read file
    with open(args[1], 'rb') as f:
        data = f.read()

    # Display hexdump
    for n, line in enumerate(hexdump(data, 'return')):
        print('{:04X}: {}'.format(n*16, line))


if __name__ == '__main__':
    main(sys.argv)
