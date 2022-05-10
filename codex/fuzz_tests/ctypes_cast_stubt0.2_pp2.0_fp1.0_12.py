import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in Python 2.7.
# See http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='django-crispy-forms',
    version=__version__,
    description='Django DRY forms.',
    long_description=open('README.rst').read(),
    author='Miguel Araujo',
    author_email='miguel.araujo.perez@gmail.com',
    url='https://github.com/maraujop/django-crispy-forms',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django>=1.4'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Aud
