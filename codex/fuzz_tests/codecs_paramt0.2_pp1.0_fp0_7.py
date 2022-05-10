import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_data(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        data = f.read()
    return data

def extract_names(data):
    return re.findall(r'\n([A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+)', data)

def main():
    names = extract_names(read_data('names.txt'))
    print(names)

if __name__ == '__main__':
    main()
