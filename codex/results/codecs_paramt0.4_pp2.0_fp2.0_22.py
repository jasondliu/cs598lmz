import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_list(src_dir):
    file_list = []
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def convert(src_dir, dst_dir, encoding):
    for file in get_file_list(src_dir):
        print('Converting file: {}'.format(file))
        with codecs.open(file, encoding='cp932', errors='strict') as f:
            text = f.read()
        with codecs.open(os.path.join(dst_dir, os.path.basename(file)), 'w', encoding=encoding, errors='strict') as f:
            f.write(text)

if __name__ == '__main__':
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
    encoding = sys.argv[3
