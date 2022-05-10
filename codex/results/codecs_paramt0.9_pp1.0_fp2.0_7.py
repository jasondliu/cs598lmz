import codecs
codecs.register_error('strict', codecs.ignore_errors)

class ConfigException(Exception): pass

def parse_list(list_string):
    return [x.strip() for x in list_string.split(',')]

def parse_dict(dict_string):
    return dict([string.split(':') for string in dict_string.split(',')])

def config_file_path(path, node='global'):
    return os.path.join(path, node + '_config.ini')

def read_config(path, node='global', format_variable=False):
    config = SafeConfigParser()
    # Use codecs to handle non-ascii characters
    with codecs.open(path, 'rb', encoding='utf-8') as f:
        config.readfp(f)

    configs = {}
    if not config.has_section(node):
        raise ConfigException('Config for %s not found in config file' % node)
    for option in config.options(node):
        if format_variable:
            configs[option.format(
