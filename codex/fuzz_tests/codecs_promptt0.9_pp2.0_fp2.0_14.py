import codecs
# Test codecs.register_error('grue', codecs.lookup_error('xmlcharrefreplace'))

import glob
import os

import cssselect
import lxml
import lxml.html
import lxml.html.builder
import lxml.html.formbuilder
import lxml.cssselect

import db

def write_template (path, tmpl, **kw):
    fd = codecs.open(path, 'w', 'utf-8')
    for line in tmpl:
        fd.write(line % kw)
    fd.close()

def read_template (path):
    fd = codecs.open(path, 'r', 'utf-8')
    tmpl = [line.rstrip() for line in fd.read()]
    fd.close()
    return tmpl

HTML_TEMPLATE = read_template('html-template.html')

CSS = '''
html {
    margin:0;
    padding:0;
}
 
body {
    font-family: sans-serif;

