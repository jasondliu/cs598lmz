import ctypes
ctypes.cast(self.handle, ctypes.c_void_p).value)
</code>
I have also seen <code>id(self.handle)</code> being suggested as a replacement; this sounds a bit better to me since it doesn't require casting to <code>c_void_p</code>, but I am not sure whether this would be stable across runs or not.


A:

In the SO Question you link to, the accepted answer is
<blockquote>
<p>You can <code>&lt;code&gt;import ctypes&lt;/code&gt;</code> and then use <code>&lt;code&gt;ctypes.cast(self.handle, ctypes.c_void_p).value&lt;/code&gt;</code>, which should give you the same value for a given <code>&lt;code&gt;self.handle&lt;/code&gt;</code>.</p>
</blockquote>
This is probably the best replacement. It has the advantage of being cross-platform, and would work even if you were using the latest version of Python.
As for your
