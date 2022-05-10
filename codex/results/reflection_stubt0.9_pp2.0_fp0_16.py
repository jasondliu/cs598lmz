fn = lambda: None
gi = (i for i in ())
fn.__code__ = ("def bar():\n    a = 1\n    b = 2\n    c = 3\n    d = 4\n    ").__code__
fn.__code__.co_freevars = ("a", "b", "c", "d",)
fn.__closure__ = (gi, )
fn()
bar()
</code>
<code>bar()</code> seems to do nothing. However, I can access the values of its cells with:
<code>fn.__closure__[0].gi_frame.f_back.f_locals["a"]
fn.__closure__[0].gi_frame.f_back.f_locals["b"]
fn.__closure__[0].gi_frame.f_back.f_locals["c"]
fn.__closure__[0].gi_frame.f_back.f_locals["d"]
</code>
where <code>a</code> returns <code>1</code>, and <code>b</code>, <code>c</code>, and <code>d</code> all return <
