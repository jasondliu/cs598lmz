import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def test_encoding():
    print(sys.stdout.encoding)
    print('中文')

def dict_to_jsonfile(dict_data, filename):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(dict_data, f, sort_keys=True, indent=4, ensure_ascii=False)
        f.write('\n')


def jsonfile_to_dict(filename):
    with open(filename, 'r', encoding='utf8') as f:
        dict_data = json.load(f)
    return dict_data


def read_all_lines(filename):
    with open(filename, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return lines


def write_all_lines(lines, filename):
    with open(filename, 'w', encoding='utf8') as f:
        f.writelines(
