import codecs
codecs.register_error('Strict_fnf_ascii', codecs.strict_errors)

if sys.version < '3':
    from ConfigParser import ConfigParser as RawConfigParser
else:
    from configparser import RawConfigParser

__all__ = ['load_config', 'load_db_config']

SCHEMA = {
    'db': {
        'database': {'required': True},
        'user': {'required': True},
        'password': {},
        'host': {'default': 'localhost'},
        'port': {},
    }
}


def load_config(config_file=None, config_location=None):
    """
    Loads the provided configuration file.

    This is a thin wrapper over the RawConfigParser constructor, to
    allow the usage of defaults in the schema and not barf up if the
    config file is missing.

    @param config_file: the file to read or a file-like object
    @param config_location: the section in the config file to load
    @return: a ConfigParser instance for the extracted section in
