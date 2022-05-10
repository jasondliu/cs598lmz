import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='django-haystack',
    version=__import__('haystack').__version__,
    description='Pluggable search for Django.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    url='http://haystacksearch.org/',
    packages=[
        'haystack',
        'haystack.backends',
        'haystack.management',
        'haystack.management.commands',
        'haystack.templatetags',
        'haystack.utils',
    ],
    package_data={
        'haystack': ['templates/search_
