import mmap
import re
import sys

if sys.version_info < (3, 0):
    import ConfigParser as configparser
else:
    import configparser

def get_config_file():
    if os.path.exists('/etc/apache2/apache2.conf'):
        return '/etc/apache2/apache2.conf'
    elif os.path.exists('/etc/httpd/conf/httpd.conf'):
        return '/etc/httpd/conf/httpd.conf'
    else:
        return None

def get_config_path():
    config_file = get_config_file()
    if config_file is not None:
        return os.path.dirname(config_file)
    else:
        return None

def get_config():
    config_file = get_config_file()
    config = {}

    if config_file is None:
        return config
    else:
        parser = configparser.ConfigParser()
        parser.read(config_file)
        config['path'] = get_config_
