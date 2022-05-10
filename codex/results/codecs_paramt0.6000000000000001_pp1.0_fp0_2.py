import codecs
codecs.register_error("strict", codecs.ignore_errors)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="my_package",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    packages=["my_package"],
    url="http://pypi.python.org/pypi/MyPackage_v010/",
    #license="LICENSE.txt",
    description="Useful towel-related stuff.",
    long_description=open("README.txt").read(),
    #install_requires=[
    #    "Django >= 1.1.1",
    #    "caldav == 0.1.4",
    #],
)

# vim: set ts=8 sw=4 sts=4 et ai tw=79:
