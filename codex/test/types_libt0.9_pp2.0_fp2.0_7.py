import types
types.FunctionType

def hello():
	pass

type(hello)

type(hello) == types.FunctionType

isinstance(hello, (types.BuiltinFunctionType, types.FunctionType))

hello.__doc__

from World.hello import hello

hello()


# 상단에 있는 from을 from . import hello로 바꿔본다.
# .은 자신 모듈을 의미한다.
# .은 .py는 빼면알아서 찾아준다.

# error
# from .hello import hello
# hello()

# error
# from ..hello import hello
# hello()


# package 
# http://docs.python.org/3/tutorial/modules.html#packages
