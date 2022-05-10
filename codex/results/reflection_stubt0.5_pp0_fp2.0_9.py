fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# E: TypeError: code object can't be used in 'exec' mode
# F: TypeError: code object can't be used in 'eval' mode
# P: TypeError: code object can't be used in 'single' mode

# The Python interpreter runs in a specific mode: either exec, eval or
# single. The mode is set by the way the Python interpreter is invoked.
# The interpreter can only execute code objects created in the same mode.
#
# When the interpreter is invoked with the -c command line option, or
# when it reads script data from standard input, it executes in
# single mode. In this mode, the code object is executed once.
#
# When the interpreter is invoked with the -m option, the code object
# is executed in the __main__ module.
#
# When the interpreter is invoked with the -i option, the code object
# is executed in the __main__ module, and the interpreter enters
# interactive mode after executing the code.
#
# When the interpreter is invoked with the -S option, the code object
# is executed in the __main__
