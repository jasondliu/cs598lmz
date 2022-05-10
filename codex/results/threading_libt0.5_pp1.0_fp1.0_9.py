import threading
threading.stack_size(67108864)

def _init():
    global _interpreter
    _interpreter = Interpreter()

_init()

def get_interpreter():
    return _interpreter

def run(script):
    global _interpreter
    _interpreter.run(script)

def eval(script):
    global _interpreter
    return _interpreter.eval(script)

def get_builtins():
    global _interpreter
    return _interpreter.builtins

def get_globals():
    global _interpreter
    return _interpreter.globals

def get_locals():
    global _interpreter
    return _interpreter.locals

def set_globals(globals):
    global _interpreter
    _interpreter.globals = globals

def set_locals(locals):
    global _interpreter
    _interpreter.locals = locals

def set_builtins(builtins
