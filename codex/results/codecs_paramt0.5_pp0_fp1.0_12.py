import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys

import setuptools
from setuptools import setup, find_packages

# Python 2.5 does not have the argparse module
if sys.version_info[:2] == (2, 5):
    import elementtree.ElementTree as ET
    import elementtree.ElementInclude as EI
    ET._original_serialize_xml = ET._serialize_xml
    def _serialize_xml(write, elem, encoding, qnames, namespaces):
        if elem.tag == EI.INCLUDE:
            xinclude = elem
            if xinclude.get('parse') == 'text':
                # text document
                text = open(xinclude.get('href')).read()
                write("<%s>%s</%s>" % (elem.tag, text, elem.tag))
                return
            else:
                # XML document
                tree = ET.parse(xinclude.get('href'))
                root = tree.getroot()
                for child in root
