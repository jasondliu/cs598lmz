import codecs
codecs.register_error('strict', codecs.ignore_errors)
</code>
The above works fine, except that I would like to replace the character at the error location with U+FFFD, or alternatively the replacement character specified in the codec's replacement field.
Is this even possible? Is there a best practice solution?


A:

I asked the same question on python-ideas. The solution added to the <code>codecs</code> document is:
<code>def xmlescape(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = [int(c) for c in exc.object[exc.start:exc.end]]
        s = ' '.join('%04x' % c for c in s)
        print('Error: %s, %s -&gt; ["%s"]' % (exc.__class__.__name__, exc, s))
    return (u'', exc.end)

codecs.register_error('strict', xmlescape)
</code>

