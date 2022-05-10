import codecs
codecs.open('/Users/johannes/Desktop/test.txt','r','utf-8')
</code>
This works fine, but when I try to open a text file that contains only ASCII characters, I get this error:
<code>UnicodeDecodeError: 'utf8' codec can't decode byte 0x80 in position 0: invalid start byte
</code>
I tried to specify the encoding as 'latin-1', but this doesn't work either. 
What am I doing wrong?


A:

You need to specify the <code>encoding</code> parameter.
<code>codecs.open('/Users/johannes/Desktop/test.txt','r','utf-8', encoding='utf-8')
</code>

