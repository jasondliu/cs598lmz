import mmap


LARGE_SIZE = 1 << 29  # 512MB

# 0 does not work.
STARTING_INDEX = 100

MODULE_NAMES = {
    'int': 'num',
    'float': 'num',
    'str': 'str',  # Quote because string is a keyword and a class.
    'list': 'list',
    'dict': 'dict',
    'tuple': 'tuple',
    'set': 'set',
    'complex': 'complex',
}


def py2nim2py(code, outfile=None):
    # import pdb; pdb.set_trace();
    if outfile is None:
        outfile = io.StringIO()

    # write the output to a StringIO which we return
    vm = AST(code)

    my_scope = Scope(vm, outfile)
    module = my_scope.global_scope(node=None, name='glob')  # Returns my_scope.

    my_scope.write('import python2nim, mmap', level=0, raw=
