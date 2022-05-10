import codecs
codecs.register_error('ignore', codecs.lookup('utf-8'))

def get_file(filename):
    if os.path.isfile(filename):
        return filename
    else:
        return os.path.join(os.path.dirname(__file__), filename)

def get_data(filename):
    f = codecs.open(get_file(filename), encoding='utf-8')
    data = f.read()
    f.close()
    return data

def get_version():
    f = open(get_file('VERSION'), 'r')
    data = f.read().strip()
    f.close()
    return data

def get_long_description():
    return get_data('README.rst')

def get_classifiers():
    return [line for line in get_data('CLASSIFIERS').split('\n') if line]

setup(
    name='django-crispy-forms',
    version=get_version(),
    description=('Django application that lets you easily build, customize '
                 'and
