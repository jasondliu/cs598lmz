import codecs
codecs.register_error('strict', codecs.ignore_errors)

from setuptools import setup, find_packages

setup(
    name='django-taggit-autosuggest',
    version='0.2.0',
    description='Autocomplete for django-taggit',
    long_description=open('README.rst').read(),
    author='Alex Hill',
    author_email='alex@alexhill.co.uk',
    url='https://github.com/alexhillc/django-taggit-autosuggest',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django-taggit>=0.9.3', 'django-autosuggest>=0.2.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
       
