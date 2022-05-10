import bz2
bz2.decompress(''.join(data['body'])).decode('utf-8')

</code>
I'm using PyMongo and when trying to insert a record I get the following error:
<blockquote>
<p>UnicodeDecodeError: 'utf8' codec can't decode byte 0x8b in position
  1: invalid start byte</p>
</blockquote>
I'm trying to figure out how to insert the record properly. Any help would be appreciated.

