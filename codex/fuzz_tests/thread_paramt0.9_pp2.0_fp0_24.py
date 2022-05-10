import sys, threading
threading.Thread(target=lambda: sys.__stdout__.write('D2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('D1\n')).start()
</code>
From a quick look at the source code, looks like <code>sys.stdout</code> is a variable that holds the default value, which is a Python file object wrapper around <code>stdout</code> C. In the main Python interpreter, this is set, whereas in subinterpreters this is not, so it's <code>None</code> by default.
The issue with passing around <code>python/Python-ast.h</code> is that it's not our job to reimplement the Python interpreter, just to use it. The main compatibility problem here is that whenever we want to disclose that <code>PyObject*</code> pointer to some Python code, we need to make sure the <code>PyThreadState</code> matches.
JIT (Numba) generates very machine specific code
We do not have to use <code>PyEval_EvalFrame</code> to execute Python code in Numba, we have
