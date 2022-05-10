import lzma
lzma.open('/path/to/file.xz')
lzma.open('/path/to/file.xz', mode='rb')
lzma.open('/path/to/file.xz', mode='wt')
lzma.open('/path/to/file.xz', mode='wt', encoding='utf-8')
lzma.open('/path/to/file.xz', mode='wt', newline='\r\n')
lzma.open('/path/to/file.xz', mode='xt')
lzma.open('/path/to/file.xz', mode='xb')
# The `x` modes is not supported, it is included for completeness.
</code>
The <code>xz.open()</code> function returns a <code>io.BufferedReader()</code> object, which can only be used to read from an opened file.
<code>import lzma
file_object = lzma.open('/path/to/file.xz')
file_object.read()

