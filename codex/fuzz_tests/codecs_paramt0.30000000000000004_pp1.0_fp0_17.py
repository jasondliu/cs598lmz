import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_contents(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

setup(
    name='django-mptt-comments',
    version=get_file_contents('VERSION'),
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A threaded comments app for Django.',
    long_description=get_file_contents('README.rst'),
    url='https://github.com/yourcelf/django-mptt-comments',
    author='Johannes Hoppe',
    author_email='info@joho.io',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language
