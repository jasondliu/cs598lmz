import codecs
codecs.register_error('strict', codecs.ignore_errors)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pymqr',
      version='0.1.1',
      description='Python MongoDB Query Runner',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='mongodb query',
      url='https://github.com/phamhongviet/pymqr',
      author='Viet Pham',
      author_email='hongvietpham@gmail.com',
      license='MIT',
      packages=['pymqr'],
      install_requires=[
          'pymongo',
      ],
      test_suite
