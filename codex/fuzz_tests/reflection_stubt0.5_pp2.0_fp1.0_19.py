fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.gi_frame.f_code
fn.__name__ = gi.gi_code.co_name = 'foo'
fn.__module__ = gi.gi_code.co_filename = 'bar'

print(fn.__name__)
print(fn.__module__)
print(fn.__code__)
print(fn.__code__.co_name)
print(fn.__code__.co_filename)

print(gi.__name__)
print(gi.__module__)
print(gi.__code__)
print(gi.__code__.co_name)
print(gi.__code__.co_filename)
</code>
output
<code>foo
bar
&lt;code object foo at 0x7f6a38b6a0a0, file "bar", line 0&gt;
foo
bar
foo
bar
&lt;code object foo at 0x7f6a38b6a0a0, file "bar", line 0&gt;
foo
bar

