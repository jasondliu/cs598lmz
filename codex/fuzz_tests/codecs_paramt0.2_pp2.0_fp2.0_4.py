import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
#   Globals
#

this_dir = os.path.dirname(__file__)

#
#   Functions
#

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

def get_version():
    version_file = os.path.join(this_dir, 'VERSION')
    return read_file(version_file).strip()

def get_long_description():
    readme_file = os.path.join(this_dir, 'README.rst')
    return read_file(readme_file)

#
#   Main
#

setup(
    name='pytest-django-queries',
    version=get_version(),
    description='A pytest plugin to help you write tests which assert the number of queries used by Django.',
    long_description=get_long_description(),
    url='https://github.com/mattrobenolt
