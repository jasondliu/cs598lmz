import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(456)

s = S()
print(s.x)
s.x = 789
print(S.x)
print(s.x)
</code>
Output:
<blockquote>
<pre><code>&lt;code&gt;456
456
789
&lt;/code&gt;</code></pre>
</blockquote>

