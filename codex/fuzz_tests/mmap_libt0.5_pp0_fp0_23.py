import mmap
import os
import re
import sys

from pygments.lexers import get_lexer_by_name
from pygments.token import Token

from . import pygments_parser

def main():
    if len(sys.argv) < 4:
        print('Usage: %s <lexer> <file> <pattern>' % sys.argv[0])
        return

    lexer_name = sys.argv[1]
    filename = sys.argv[2]
    pattern = sys.argv[3]

    if not os.path.exists(filename):
        print('File %s does not exist' % filename)
        return

    lexer = get_lexer_by_name(lexer_name)
    pattern = re.compile(pattern)
    parser = pygments_parser.PygmentsParser(lexer, pattern)

    with open(filename, 'r') as f:
        mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        for match in parser.finditer(
