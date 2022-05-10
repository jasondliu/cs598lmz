import _struct
import types

from binascii import b2a_base64

from version_info import version as version_info


class ASPN_mod_python:
    """
    An ASPN module subclassed to publish the ASPN website.
    """

    dir = os.path.dirname(__file__)
    pysa_mod_python_dir = os.path.dirname(dir)
    cgi_dir = os.path.dirname(pysa_mod_python_dir)
    includes = [cgi_dir]
    pysa_pylibs_dir = os.path.dirname(cgi_dir)
    pysa_dir = os.path.dirname(pysa_pylibs_dir)
    pylibs_dir = os.path.dirname(pysa_dir)
    display_errors = True
    display_exceptions = True
    uri = '/asynchat2/'

