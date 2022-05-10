from types import FunctionType
list(FunctionType('func', {}).__dir__())

def func():
    pass
" | python3

echo "
from types import FunctionType
list(FunctionType('func', {}).__dir__())
" | python3

function allBuiltin {
    python3 -c "
import sys, re

funclist = [ repr(i) for i in dir(sys.modules[sys.builtin_module_names[0]]) \\
                          if re.match('[_[:alpha:]]', i)]
funcliststring = ' \\\n  '.join(funclist)
print(' function %s { \\'%sys.argv[1])
print('    python3 -c " \\')
print('print( %s )\\'%funcliststring)
print('print( type(%s) )\\'%sys.argv[1])
print('print( id(%s) )\\'%sys.argv[1])
print('" \\')
print('}')
 "
}

allBuiltin abs
