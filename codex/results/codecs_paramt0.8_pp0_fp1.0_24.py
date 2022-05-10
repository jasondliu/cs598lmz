import codecs
codecs.register_error('surrogate_escape', codecs.ignore_errors)


def load_config():
    """
    Load the config
    :return:
    """
    logging.info("Loading Config from file %s" % config.DEFAULT_CONFIG_FILE)
    with open(config.DEFAULT_CONFIG_FILE, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    return cfg


def load_class(class_type, module_name, class_name):
    """
    Load a class when you only know the class name
    :param class_type:
    :param module_name:
    :param class_name:
    :return:
    """
    try:
        found = importlib.import_module(module_name)
        return getattr(found, class_name)
    except AttributeError as e:
        logging.error("Class %s not found in module %s" % (class_name, module_name))
        raise e


def load_module(module_name):
    try:

