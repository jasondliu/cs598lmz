import codecs
codecs.open("myFile.txt", ...
</code>
That will give the default encoding (presumably, UTF-8 those days).
If you need Unicode and can live with UTF-8 and latin-1, you can use this which tries latin-1 if it can't properly decode from UTF-8:
<code>def text_or_bytes(myfile):
    try:
        return myfile.read().encode('utf-8')
    except UnicodeError:
        return myfile.read().encode('latin-1')
</code>
Otherwise, if you are going to be explicit about the encoding, then use 
<code>codecs.open("myFile.txt", 'rb', 'utf8')
</code>
(or whatever encoding you have in mind). Oh, and <code>'rb'</code> because your file may have binary content in it.
What to use when all else fails is a black art, although people do have tables of best encodings to use when the file is of a certain bytes-encoding.
There is a similar recipe on the Cookbook, although it's not
