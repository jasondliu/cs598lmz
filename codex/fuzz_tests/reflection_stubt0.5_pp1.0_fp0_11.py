fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_filename = gi.gi_code.co_filename = '&lt;stdin&gt;'

import dis
dis.dis(fn)
</code>
Output:
<code>  1           0 LOAD_GLOBAL              0 (None)
              3 RETURN_VALUE
</code>

