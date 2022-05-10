import types
types.ModuleType.__repr__ = lambda self: self.__name__

from [% libname %] import *

# We can pre-set the settings for the module.
[% IF libname.contains("lib") %]
settings.module_settings = settings.read_settings("""
{
  "libname": {
    "my_setting": "my_value"
  }
}
""")
[% END %]

# Run the test function.
[% libname %].test()

# Run the main function.
[% libname %].main()

# If you want to install this module so it can be imported, use the setup.py
# file.
setup(
  name='[% libname %]',
  version='0.0.1',
  description='My [% libname %] package',
  author='[% author %]',
  author_email='[% email %]',
  url='https://github.com/[% github %]',
  install_requires=[
    'cloudmesh-common',
 
