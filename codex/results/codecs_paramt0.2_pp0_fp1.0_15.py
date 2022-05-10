import codecs
codecs.register_error('strict', codecs.ignore_errors)

from setuptools import setup, find_packages

setup(
    name='django-sphinxdoc',
    version='0.1.1',
    description='Django app to integrate Sphinx documentation into your project.',
    long_description=open('README.rst').read(),
    author='Jannis Leidel',
    author_email='jannis@leidel.info',
    url='http://github.com/jezdez/django-sphinxdoc/',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
