import lzma
lzma.decompress(t)
Warning when running lzma on Python 2.7.13 : 
UnicodeDecodeError: 'utf8' codec can't decode bytes in position 0-1: unexpected end of data
If I convert t in bytes, the script is working fine.
The problem is that I won't to run this script on Python 3 environment and this script is not working there (I got the error : TypeError: a bytes-like object is required, not 'str')
Do you know if I can convert my t into bytes type while it consists on ascii caracters ?
Thanks in advance.


A:

I find the solution.
In fact, I found that my t was in bytes type after I run :
<code>Type(t)
</code>
Then, I just run :
<code>lzma.decompress(t.encode())
</code>
And it worked.
Thank for helping me.

