import codecs
codecs.register_error('strict', codecs.ignore_errors)

def fix_encoding(s):
    return s.encode('latin1').decode('utf8')

def read_data(filename):
    with open(filename, 'r', encoding='latin1') as f:
        return [fix_encoding(line.strip()) for line in f.readlines()]

def write_data(filename, data):
    with open(filename, 'w', encoding='utf8') as f:
        for line in data:
            f.write(line + '\n')

def main(argv):
    infile = argv[0]
    outfile = argv[1]
    data = read_data(infile)
    write_data(outfile, data)

if __name__ == '__main__':
    main(sys.argv[1:])
