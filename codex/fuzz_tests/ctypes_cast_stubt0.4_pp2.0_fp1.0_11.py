import ctypes
ctypes.cast(0, ctypes.py_object)

# ______________________________________________________________________

if __name__ == "__main__":
    import unittest
    from . import test_ast as ast_test
    from . import test_builtin as builtin_test
    from . import test_bytecode as bytecode_test
    from . import test_compile as compile_test
    from . import test_eval as eval_test
    from . import test_exec as exec_test
    from . import test_import as import_test
    from . import test_int as int_test
    from . import test_literal as literal_test
    from . import test_long as long_test
    from . import test_misc as misc_test
    from . import test_module as module_test
    from . import test_parser as parser_test
    from . import test_peephole as peephole_test
    from . import test_stmt as stmt_test
    from . import test_symtable as symtable_test
    from . import test_token as token_test
    from .
