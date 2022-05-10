import ctypes
ctypeslib = importlib.import_module("ctypeslib")
c = ctypeslib.codegen.ctypedescs.CTypesVisitor("status.h")
assert False
