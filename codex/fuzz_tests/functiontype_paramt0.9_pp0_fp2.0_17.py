from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure) for f in [lambda a,b:c for a,b,c in []])
a
f.func_closure[0].cell_contents
f.__closure__[0].cell_contents
f.__closure__

{0: (1 / (1 - 1))}.items()
amusement_park()
if __name__ == '__main__':
    str('\n'.join(map(str, amusement_park())))
amusement_park()
str('\n'.join(map(str, amusement_park())))
exit()
exit(0)
exit(1)
exit(0)
# TODO How to ask for input from the user?
# TODO Show how to do a %run command

# TODO Show how to set the working directory
import os
os.path.dirname(__file__)
os.path.dirname(__file__).split(os.sep)
os.
