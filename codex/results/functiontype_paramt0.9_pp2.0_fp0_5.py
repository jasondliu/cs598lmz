from types import FunctionType
list(FunctionType(lambda x: x).__globals__)

\end{verbatim}

\noindent Running this piece of code in a local IPython session, we get:

\begin{verbatim}
In [1]: list(FunctionType(lambda x: x).__globals__)
Out[1]: ['__builtins__']
\end{verbatim}

\noindent By default, the context in which Python functions are compiled does not include any variables from the \verb|__main__| module.

Now, let us define a function with access to the \verb|foo| variable:

\begin{verbatim}
In [2]: def func_with_foo():
   ...:     leaf1_foo = foo
   ...:     return leaf1_foo - 1
   ...:
   ...:
\end{verbatim}

\noindent and inspect the context its bytecode was compiled with:

\begin{verbatim}
In [3]: list(FunctionType(func_with_foo.__code__).__globals__)
