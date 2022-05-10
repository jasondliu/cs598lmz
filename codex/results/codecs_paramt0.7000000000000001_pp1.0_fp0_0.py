import codecs
codecs.register_error("xmlcharrefreplace", xmlcharrefreplace)

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class ReST2html():
    def __init__(self, input_file, output_file=None, template=None, theme='default', title=''):
        bf = BuilderFactory()
        if template:
            self.builder = bf.get_builder(Reader(), template)
        else:
            self.builder = bf.get_builder(Reader(), 'default.html')
        self.builder.theme = theme
        self.builder.filename = input_file
        if output_file:
            self.builder.output_filename = output_file
        else:
            self.builder.output_filename = input_file + ".html"
        self.builder.title = title

    def convert(self):
        try:
            f =
