fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
</code>
Try it:
<code>&gt;&gt;&gt; fn()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'generator' object is not callable
</code>
The cause is that the object <code>fn.__code__</code> is a generator code object, so the Python VM executes <code>fn()</code> with the builtin callable <code>call_generator()</code> in ceval.c:
<code>static PyObject *
call_function(PyObject ***pp_stack, int oparg
#ifdef WITH_TSC      /* see ceval.c */
    , uint64* pintr0, uint64* pintr1
#endif
    )
{
    PyObject **pfunc, *func, *x, *w;
    PCALL(PCALL_FUNCTION);
    Py_GUARD();
    pfunc = (*pp_stack)-1;
    func =
