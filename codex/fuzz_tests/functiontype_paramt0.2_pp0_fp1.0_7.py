from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
import dis
dis.dis(lambda: None)

# bytecode
import marshal
marshal.loads(marshal.dumps(lambda: None.func_code))

# function attributes
lambda: None.func_defaults
lambda: None.func_closure
lambda: None.func_globals
lambda: None.func_dict
lambda: None.func_name
lambda: None.func_doc
lambda: None.func_code

# callable objects
class C(object):
    def __call__(self):
        pass
C()

# callable objects
class C(object):
    def __call__(self):
        pass
C()()

# callable objects
class C(object):
    def __call__(self):
        pass
C()()()

# callable objects
class C(object):
    def __call__(self):
        pass
C()()()()

# callable objects
class C(object):
    def __call
