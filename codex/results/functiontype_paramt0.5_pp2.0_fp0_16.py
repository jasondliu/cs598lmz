from types import FunctionType
list(FunctionType(lambda: None).__dict__)

# list of all built-in functions
import builtins
list(builtins.__dict__)

# list of all built-in functions that start with "s"
import builtins
list(filter(lambda x: x.startswith('s'), builtins.__dict__))

# list of all built-in functions that are defined in the builtins module
import builtins
list(filter(lambda x: x.__module__ == 'builtins', builtins.__dict__))

# list of all built-in functions that are defined in the builtins module and start with "s"
import builtins
list(filter(lambda x: x.__module__ == 'builtins' and x.startswith('s'), builtins.__dict__))

# list of all built-in functions that are defined in the builtins module and start with "s" and are callable
import builtins
list(filter(lambda x: x.__module__ == 'builtins' and x.startswith('s') and callable(x), builtins.__dict__
