from types import FunctionType
list(FunctionType(code, globals())() for code in (compile("""
def f():
    return 1
""", '<string>', 'exec'), compile("""
def f():
    return 2
""", '<string>', 'exec')))

# New in Python 3.6:
#   - PEP 526: Syntax for variable annotations
#   - PEP 525: Asynchronous generators

# New in Python 3.7:
#   - PEP 515: Underscores in numeric literals
#   - PEP 523: Postponed evaluation of annotations
#   - PEP 526: Syntax for variable annotations
#   - PEP 544: Single-dispatch generic functions
#   - PEP 545: Python language server protocol
#   - PEP 550: Context Variables
#   - PEP 557: Data Classes
#   - PEP 562: Module __getattr__ and __dir__
#   - PEP 563: Postponed evaluation of type annotations
#   - PEP 564: Additional unpacking generalizations
#   - PEP 567: Context
