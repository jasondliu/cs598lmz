import codecs
codecs.open("test.html", encoding='utf-8')
</code>

So what encoding is Japanese. I've tried 'utf-8' but then katakana words are broken. Maybe 'ascii' is right but I get an an error: 
<blockquote>
<p>UnicodeEncodeError: 'ascii' codec can't encode character u'\u8d85' in
  position 6: ordinal not in range(128)</p>
</blockquote>


A:

I'm going to go out on a limb here and say that probably the problem is the following:
<code>&gt;&gt;&gt; soup = BeautifulSoup(params.word)
&gt;&gt;&gt; print soup.encode('utf-8')
�����������
&gt;&gt;&gt; print params.word
イエローページ
</code>
You are using the <code>.word</code> property as a byte-string. If you want to process it as a Unicode string, you're going to have to decode it:
<code
