import codecs
codecs.register_error('strict', codecs.ignore_errors)

def print_usage():
    print 'Usage:', sys.argv[0], '<input file> <output file>'

def main():
    if len(sys.argv) != 3:
        print_usage()
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with codecs.open(input_file, 'r', 'utf-8', 'strict') as f:
        input_text = f.read()

    output_text = input_text.replace(u'\u00a0', u' ')

    with codecs.open(output_file, 'w', 'utf-8', 'strict') as f:
        f.write(output_text)

if __name__ == '__main__':
    main()
