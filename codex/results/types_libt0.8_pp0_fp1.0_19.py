import types
types.__name__

#from types import __name__
#AttributeError: 'module' object has no attribute '__name__'

#from types import \__name__
#SyntaxError: unexpected character after line continuation character

from types import __name__ as typeName
typeName

#from types import __name__, __file__
#SyntaxError: invalid syntax

from types import __name__, __file__ as typeInfo
typeInfo

from types import __name__ as typeName, __file__ as typeInfo
typeInfo, typeName

from types import __name__ as typeName, __file__ as typeInfo
typeInfo, typeName

#from types import __name__, __file__
#SyntaxError: invalid syntax

from types import __name__, __file__ as typeInfo
typeInfo

#from types import __name__ as typeName, __file__
#SyntaxError: invalid syntax

from types import __name__ as typeName, __file__ as typeInfo
typeInfo, typeName

#from types import __name__ as typeName, __file__
