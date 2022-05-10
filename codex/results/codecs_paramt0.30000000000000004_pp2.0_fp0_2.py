import codecs
codecs.register_error('strict', codecs.ignore_errors)

import logging
logger = logging.getLogger(__name__)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(filename, contents):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(contents)

def read_json_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return json.load(f)

def write_json_file(filename, contents):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        json.dump(contents, f, indent=2, sort_keys=True)

def read_yaml_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
