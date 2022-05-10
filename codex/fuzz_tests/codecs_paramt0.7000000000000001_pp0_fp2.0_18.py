import codecs
codecs.register_error("strict", codecs.ignore_errors)

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from django_core import __version__


setup(name='django-core',
      version=__version__,
      description='A set of reusable Django apps',
      author='Django Core Team',
      author_email='webmaster@djangocore.com',
      url='http://github.com/django-core/django-core',
      license='BSD',
      packages=find_packages(),
      # package_dir={'django_core': 'django_core'},
      include_package_data=True,
      zip_safe=False,
      classifiers=[
        'Development Status :: Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic
