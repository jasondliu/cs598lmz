import codecs
# Test codecs.register_error
import codecs
import re
def word_repl_func(exc):
    if isinstance(exc, codecs.UnicodeReplacementError):
        return (u'%%UNICODE%%', exc.start + 6)
    else:
        # Same as the default handler for other codecs.
        # See http://docs.python.org/lib/bltin-codec-base.html.
        return (u'', exc.start + 1)
codecs.register_error('wordreplace', word_repl_func)
encoding = 'ascii'
for text in [u'abc\uFFFDdef', u'abc \uFFFD def']:
    print text
    print text.encode(encoding, 'wordreplace')
</code>
Output
<code>abc�def
abc%%UNICODE%%def
abc � def
abc %%UNICODE%% def
</code>
http://docs.python.org/library/codecs.html

