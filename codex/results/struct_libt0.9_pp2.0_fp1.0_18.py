import _struct

ROOT_DIR = os.path.abspath(".")


def load_json(json_path):
    '''
    load a json file and return the python object
    '''
    with open(json_path, encoding='utf-8') as file:
        data = json.load(file, object_pairs_hook=OrderedDict)
    return data


def list_files(dirpath, exts):
    '''
    Find files whose extension is in exts.
    exts: List[str]
    '''
    files = os.listdir(dirpath)
    # print(files)  # ['testdata.json', 'test_data.py']
    # print(exts)  # ['.py', '.json']
    # os.path.join() will put absolute path in linux, and dirpath belong to
    # the project's root path. So here is ROOT_DIR, not dirpath.
    files = [os.path.join(ROOT_DIR, 
                          dirpath, fname) for fname in files
