import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(input_file):
    with codecs.open(input_file, 'r', 'utf-8', 'ignore') as f:
        return f.read()

def write_file(output_file, data):
    with codecs.open(output_file, 'w', 'utf-8', 'ignore') as f:
        f.write(data)

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data = read_file(input_file)
    data = data.replace('\r\n', '\n')
    write_file(output_file, data)

if __name__ == '__main__':
    main()
