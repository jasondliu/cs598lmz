import _struct
import _sockio
import _sre
import _symtable
import _sysconfig


"""These modules all use some unimplemented feature."""

_no_examples = set(['BaseHTTPServer', 'Bastion', 'Canvas', 'Hotshot',
                    'HTMLParser', 'hmac', 'ihooks', 'lib-tk', 'pydoc_data',
                    'regsub', 'tkColorChooser', 'tkCommonDialog',
                    'tkFileDialog', 'tkSimpleDialog', 'turtle', 'wave',
                    ])

_extra_info = {
    "pydoc":  ("See pydoc documentation.",
               "apt:python-defaults"),
    }

def extract_info_example(fname):
    """
    Extract the docstring, and the first pythonic example.
    """
    with open(fname) as fobj:
        lines = fobj.readlines()

    docs = []
    examples = []
    in_doc = False
