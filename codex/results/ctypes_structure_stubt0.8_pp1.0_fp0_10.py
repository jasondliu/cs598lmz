import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int8
    y = ctypes.c_int16

print ctypes.sizeof(S)
</code>
Results with python 2.7:
<blockquote>
<pre><code>&lt;code&gt;python test.py
3
&lt;/code&gt;</code></pre>
</blockquote>
Results with python 3.3:
<blockquote>
<pre><code>&lt;code&gt;python3 test.py
4
&lt;/code&gt;</code></pre>
</blockquote>

That behavior is expected.
In python 2.7, ctypes uses the quiet "C" alignment policy.
In python 3.3, ctypes uses the stricter "native" alignment policy.

From the C Standard:
<blockquote>
<p><strong>6.2.8 Representations of types</strong></p>
<p>[...]</p>
<p>22 A pointer to void shall have the same representation and alignment requirements as a pointer to a character type.</p>
<p>23 Pointers to structure
