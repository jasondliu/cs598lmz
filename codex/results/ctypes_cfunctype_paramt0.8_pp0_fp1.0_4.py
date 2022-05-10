import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
def myfun(n):
    print n
    return n + 1

fun1 = FUNTYPE(myfun)

for i in range(10):
    fun1(i)



#Python API
#http://docs.python.org/2/library
#http://docs.python.org/2/extending/extending.html

import sys
sys.argv
sys.path

#The Python Interpreter
#
#The interpreter operates somewhat like the UNIX shell: when called with standard input connected to a tty device, it reads and executes commands interactively; 
#when called with a file name argument or with a file as standard input, it reads and executes a script from that file.
#A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, analogous to the shell’s -c option.

#Since Python statements often contain spaces or other characters that are special to the shell, it is best to quote command in its entirety with single quotes.

#!
