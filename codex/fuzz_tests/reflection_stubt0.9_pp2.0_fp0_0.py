fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi
fn.__code__

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/site-packages/scitools/easyviz/common.py", line 81, in _try_abort_if_matplotlib_is_importing
    raise AssertionError("Error: matplotlib is being imported while "
AssertionError: Error: matplotlib is being imported while easyviz is being imported. This may cause problems with Easyviz, as it will hide the presence of mpl. There are a large number of such cases where packages conflict and easier usage has been sacrificed in the name of 'strict adherence to standards'. Please report situation to scitools.easyviz@gmail.com (SciTools - Yun-Jhong Wu), but do include how to fix the situation.
</code>
The assertion happens in som code at which I'm not looking now, but the point is that the assertion is not raised when I delete the for loop.
