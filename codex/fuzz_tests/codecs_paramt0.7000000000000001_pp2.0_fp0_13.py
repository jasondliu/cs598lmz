import codecs
codecs.register_error('ignore', codecs.lookup('ignore'))

# Open file to write html
f = codecs.open('file.html','w','utf-8','ignore')

# Write header
f.write('&lt;html&gt;\n&lt;head&gt;\n&lt;title&gt;Title&lt;/title&gt;\n&lt;/head&gt;\n&lt;body&gt;')

# Write body
f.write(unicode('&lt;h2&gt;Title&lt;/h2&gt;\n', 'utf-8'))

# Close file
f.close()
</code>
On this line:
<code>f.write(unicode('&lt;h2&gt;Title&lt;/h2&gt;\n', 'utf-8'))
</code>
It gives me this error:
<code>Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    f.write(unicode('&lt;
