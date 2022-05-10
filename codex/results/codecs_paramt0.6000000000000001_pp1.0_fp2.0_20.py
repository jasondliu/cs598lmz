import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename, file_encoding='utf-8'):
    data = []
    for line in codecs.open(filename, encoding=file_encoding):
        data.append(line)
    return data

def main():
    data = get_data('test.txt')
    print(data)

if __name__ == '__main__':
    main()
