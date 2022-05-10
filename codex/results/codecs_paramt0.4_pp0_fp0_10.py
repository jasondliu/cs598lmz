import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_data(filename):
    with codecs.open(filename, encoding='utf-8', mode='r', errors='replace_with_space') as f:
        data = f.read()
    return data

def extract_names(data):
    return re.findall(r'\n([A-Z][a-z]{1,}) [A-Z][a-z]{1,}', data)

def main():
    names = extract_names(read_data('names.txt'))
    print(sorted(set(names)))

if __name__ == "__main__":
    main()
