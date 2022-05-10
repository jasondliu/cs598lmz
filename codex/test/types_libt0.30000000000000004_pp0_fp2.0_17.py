import types
types.ModuleType.__dict__.update(dict)

def get_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def get_config_value(key):
    config = get_config()
    return config[key]

def get_config_value_from_file(file_path, key):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config[key]

def get_config_value_from_string(config_string, key):
    config = json.loads(config_string)
    return config[key]

