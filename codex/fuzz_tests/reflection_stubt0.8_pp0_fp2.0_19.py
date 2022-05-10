fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__ = gi
""")

    def test_code_assignment_with_code_like(self):
        self.assertCodeExecution("""
class CodeLike:
    def __init__(self):
        self.co_argcount = 0
        self.co_filename = 'file'
        self.co_firstlineno = 0
        self.co_flags = 0
        self.co_lnotab = 'lnotab'
        self.co_name = 'func'
        self.co_names = ()
        self.co_stacksize = 0
        self.co_varnames = ()
        self.co_cellvars = ()
        self.co_freevars = ()

codelike = CodeLike()
fn = lambda: None
fn.__code__ = codelike
fn.__code__ = codelike
""")

    def test_unhashable_code_assignment(self):
        self.assertCodeExecution("""
fn = lambda: None
fn.__code__ = "hello
