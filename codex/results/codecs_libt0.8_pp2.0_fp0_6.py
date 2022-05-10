import codecs
codecs.register_error('my_strict', codecs.ignore_errors)

def _save_hash_file(path, hash_dict, encoding='utf8'):
    with codecs.open(path, 'w', encoding, 'my_strict') as f:
        f.write(json.dumps(hash_dict, ensure_ascii=False))

def _save_pkl_file(path, obj):
    with codecs.open(path, 'wb') as f:
        pickle.dump(obj, f)

def _load_pkl_file(path):
    with codecs.open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj

def _save_file(path, obj, encoding='utf8'):
    with codecs.open(path, 'w', encoding, 'my_strict') as f:
        if isinstance(obj, list):
            f.write("\n".join(obj))
        elif isinstance(obj, dict):
            f.write("\
