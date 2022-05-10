import codecs
codecs.open(filename, encoding='utf-8')
</code>
If you need to use the file with <code>open()</code>, you can wrap the file object in a <code>codecs.StreamReader</code>:
<code>open(filename, 'rb') as f:
    encoded_text = unicode(f.read(), 'utf-8')
</code>

