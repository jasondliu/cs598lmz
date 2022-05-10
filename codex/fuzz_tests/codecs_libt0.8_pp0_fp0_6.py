import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

global_config = None

def read_config_file(config_path):
    import configparser
    global global_config
    if not global_config:
        global_config = configparser.ConfigParser()
        global_config.read(config_path)
        if not global_config.has_section('core'):
            global_config.add_section('core')
        if not global_config.has_option('core', 'work_dir'):
            global_config.set('core', 'work_dir', os.getcwd())
        if not global_config.has_section('templates'):
            global_config.add_section('templates')
        if not global_config.has_option('templates', 'dir'):
            global_config.set('templates', 'dir', os.path.dirname(os.path.dirname(settings.__file__)))
        if not global_config.has_option('templates', '
