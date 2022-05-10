import codecs
codecs.register_error('interpolate', interpolate_forward)
dest_tx  = codecs.getreader('win1251')(source, errors='interpolate')
</code>
...which I expect to produce a u'\xbf\xf4\xbf\xe2\xbf\xf0\xbf\xee\xbf\xea \xbf\xf0\xbf\xee\xbf\xed\xbf\xf2\xbf\xf0 \xbf\xf0\xbf\xe5\xbf\xee\xbf\xf3 \xbf\xe7\xbf\xed\xbf\xed\xbf\xe5\xbf\xe7\xbf\xe0' in Windows 1251, but instead it throws this error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "codecs.py", line 351, in getreader
    return lookup(encoding).streamreader
LookupError: unknown error handler name 'inter
