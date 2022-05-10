import codecs
codecs.register_error('surrogate_or_special', codecs.surrogateescape)

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='surrogate_or_special') as f:
        return f.read()

def write_file(filename, contents):
    with codecs.open(filename, 'w', encoding='utf-8', errors='surrogate_or_special') as f:
        f.write(contents)

def main():
    if len(sys.argv) != 3:
        print('Usage: python3 fix_encoding.py <input_file> <output_file>')
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    contents = read_file(input_file)
    write_file(output_file, contents)

if __name__ == '__main__':
    main()
