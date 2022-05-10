import lzma
lzma.get_timer_func()
-&gt; &lt;built-in function get_timer_func&gt;
lzma.get_timer_func(1)
-&gt; &lt;built-in function get_timer_func&gt;
lzma.get_timer_func(None)
-&gt; None
</code>
You can revert this by reassigning the function back:
<code># Reset the timer function.
lzma.get_timer_func(None)
# Verify.
lzma.get_timer_func(1)
lzma.get_timer_func()
# Compress data.
with lzma.open(...) as f:
    ...
# Ensure it didn't crash.
</code>

Note that you can also set the timer function before importing the <code>lzma</code> module:
<code>lzma.set_timer_func(None)
import lzma
with lzma.open(...) as f:
    ...
</code>

