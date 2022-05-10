from lzma import LZMADecompressor
LZMADecompressor()

# Imports come after the magic.
from lib2to3 import fixer_base, pytree
from lib2to3.pgen2 import token
from lib2to3.pytree import Leaf, Node
from lib2to3.pygram import python_symbols as syms


class FixDecompress(fixer_base.BaseFix):
    BM_compatible = True
    order = "pre"

    PATTERN = """
    power< 'decompress'
        trailer< dot='.' meth='decompress'>
        trailer< '(' arg=any ')' >
    >
    """

    def transform(self, node, results):
        assert results
        if node.parent.type is not syms.simple_stmt:
            return

