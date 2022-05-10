import codecs
codecs.register_error('surrogate_or_special', surrogatepass)

def read_data(filename):
    with codecs.open(filename, "r", encoding='utf8') as f:
        data = f.read()
    return data

def extract_names(data):
    names = re.findall(r'\n([A-Z][a-z]{1,})', data)
    return names

def main():
    names = extract_names(read_data('data/names.txt'))
    print(names)
    print(len(names))

if __name__ == '__main__':
    main()
