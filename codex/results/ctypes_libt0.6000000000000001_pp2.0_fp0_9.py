import ctypes
ctypes.cdll.LoadLibrary("libclang.so")

from clang.cindex import Index
from clang.cindex import CursorKind

class CodeGen(object):
    def __init__(self, filename, code_file_name, debug=False):
        self.code_file_name = code_file_name
        self.debug = debug
        self.index = Index.create()
        self.ast = self.index.parse(filename)
        self.code = self.parse()

    def parse(self):
        code = ""
        for c in self.ast.get_children():
            code += self.dispatch(c)
        return code

    def dispatch(self, c):
        kind = c.kind
        if kind == CursorKind.FUNCTION_DECL:
            return self.visitFunctionDecl(c)
        elif kind == CursorKind.CXX_METHOD:
            return self.visitCXXMethod(c)
        elif kind == CursorKind.CLASS_DECL:
            return self.visitClassDecl(
