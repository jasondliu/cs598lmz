fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
</code>
This throws:
<code>TypeError: 'cell' object is not callable
</code>
I'm not finding anything in the Python docs on what the <code>cell</code> object is and why it's not callable. Is there a way to get this code to execute?
<blockquote>
<p><strong>Solution</strong></p>
<p>Use <code>&lt;code&gt;eval&lt;/code&gt;</code>.</p>
</blockquote>


A:

This is not a solution to get the code to execute, but instead an explanation for the error.
The <code>TypeError</code> is raised in <code>call_function</code> from <code>ceval.c</code>. One of the occurrences is in the line labeled <code>CALL_FUNCTION</code>.
<code>static PyObject *
call_function(PyObject ***pp_stack, int oparg, int na, int nk)
{
    PyObject **pfunc = (*pp_stack) - na - n
