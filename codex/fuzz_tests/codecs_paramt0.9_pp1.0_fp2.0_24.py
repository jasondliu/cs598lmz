import codecs
codecs.register_error('replace_nbsp', lambda err, *args: (u'?', err.start+1))
file = codecs.open(path, 'r', 'utf-8', 'replace_nbsp')
</code>
See the error handling section of the <code>codecs</code> documentation, look for "Registering an error handler".
You'd need the <code>lines</code> sequence if you wanted to handle the file line-by-line; since you're only processing the file once, that's not necessary here.

