import codecs
codecs.register(chardet.search_function)

import sys

def read_file(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
            result = chardet.detect(data)
            return data.decode(result['encoding'])
    except Exception as e:
        print(e)
        return None

def write_file(filename, data):
    try:
        with open(filename, 'wb') as f:
            f.write(data.encode('utf-8'))
            return True
    except Exception as e:
        print(e)
        return False

def remove_file(filename):
    try:
        os.remove(filename)
        return True
    except Exception as e:
        print(e)
        return False

def preprocess(input_file, output_file):
    # Read file
    data = read_file(input_file)
    if not data:
        return 1

    # Remove \r
    data = data.replace('\
