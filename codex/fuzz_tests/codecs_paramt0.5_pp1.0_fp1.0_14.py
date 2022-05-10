import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(file_name):
    with codecs.open(file_name, 'r', encoding='utf-8', errors='replace_with_space') as f:
        text = f.read()
    return text

def write_file(file_name, text):
    with codecs.open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    text = read_file('test.txt')
    text = text.replace('\r', '')
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    write_file('test_out.txt', text)

if __name__ == '__main__':
    main()
