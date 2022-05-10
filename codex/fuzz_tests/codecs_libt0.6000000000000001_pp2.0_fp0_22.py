import codecs
codecs.encode(b'\xe4', 'cp65001')
</code>
<blockquote>
<p>UnicodeEncodeError: 'cp65001' codec can't encode character '\xe4' in
  position 0: character maps to undefined</p>
</blockquote>


A:

You are trying to encode a byte string (<code>b'\xe4'</code>) as a character string (<code>'cp65001'</code>).
The <code>codecs.encode</code> function encodes character strings as byte strings. You need to decode the byte string first:
<code>codecs.encode(codecs.decode(b'\xe4', 'utf-8'), 'cp65001')
</code>

