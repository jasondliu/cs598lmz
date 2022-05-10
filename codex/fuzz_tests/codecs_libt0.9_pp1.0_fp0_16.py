import codecs
codecs.register(lambda name: codecs.lookup("utf-8") if name == "cp65001" else None)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#if sys.argv[-1] == 'publish':
    #os.system('python setup.py sdist upload')
    #sys.exit()

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst", "r") as history_file:
    history = history_file.read()

setup(name='cobra_measurement',
      version="0.0.1",
      description="COBRA medical image measurement",
      long_description=readme + '\n\n' + history,
      author="Patrice Guyennet",
      author_email="guyennet.patrice@gmail.com",
      url="https://github.com/SintefMath/cobra-measurement",
