import codecs
codecs.register_error('strict', codecs.ignore_errors)

def load_config(path):
    # Load config file
    with open(path, 'r') as f:
        config = yaml.load(f)

    # Load config from environment variables
    for k, v in config.items():
        if isinstance(v, str):
            config[k] = os.getenv(k, v)

    return config


def load_data_json(path, encoding='utf8'):
    with codecs.open(path, 'r', encoding=encoding, errors='strict') as f:
        return json.load(f)


def save_data_json(data, path, encoding='utf8'):
    with codecs.open(path, 'w', encoding=encoding, errors='strict') as f:
        json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)


def load_data_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load
