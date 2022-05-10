gi = (i for i in ())
# Test gi.gi_code.co_flags & CO_GENERATOR
#   (identifies generators as a distinct class)
print(type(gi))
</code>
Output:
<code>&lt;class 'generator'&gt;
</code>

