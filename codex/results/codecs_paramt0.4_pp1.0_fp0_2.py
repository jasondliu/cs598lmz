import codecs
codecs.register_error('strict', codecs.ignore_errors)

from optparse import OptionParser
import sys

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def main():
    parser = OptionParser()
    parser.add_option('-l', '--lexer', dest='lexer',
                      help='name of the lexer to use')
    parser.add_option('-f', '--formatter', dest='formatter',
                      help='name of the formatter to use')
    parser.add_option('-o', '--outfile', dest='outfile',
                      help='file to write to (defaults to stdout)')
    parser.add_option('-F', '--full', action='store_true', dest='full',
                      help='use the full formatter')
    parser.add_option('-L', '--linenos', action='store_true', dest='linenos',
                      help='activate line numbers')
    parser.add_option('-H', '--hl
