import codecs
codecs.register_error('strict', codecs.strict_errors)

def fpath(f):
    return os.path.join(os.path.dirname(__file__), f)

def read(f):
    return codecs.open(fpath(f), 'r', 'utf-8').read()

def version():
    f = fpath('src/social_network/__init__.py')
    return re.search(r"""^__version__\s*=\s*['"]([^'"]*)['"]""", read(f), re.M).group(1)

setup(
    name='social_network',
    version=version(),
    author='Johnathan Jenkins',
    author_email='jenkins.johnathan@gmail.com',
    packages=['social_network'],
    package_dir={'social_network': 'src/social_network'},
    scripts=['src/social_network/social_network.py'],
    url='https://github.com/Johnathan-Jenkins/SocialNetwork',
    license='MIT',
    description
