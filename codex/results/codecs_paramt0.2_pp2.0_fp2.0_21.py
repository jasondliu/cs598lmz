import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        return f.read()

def write_file(filename, text):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

def main():
    if len(sys.argv) != 3:
        print('Usage: %s <input file> <output file>' % sys.argv[0])
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    text = read_file(input_file)
    text = re.sub(r'\s+', ' ', text)
    write_file(output_file, text)

if __name__ == '__main__':
    main()
