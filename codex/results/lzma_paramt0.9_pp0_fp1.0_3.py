from lzma import LZMADecompressor
LZMADecompressor.decompress(open('huge_file.xz','rb').read()).decode('utf-8')
</code>
Tendrás que llamar a esa función cada vez que quieras desempaquetar cada uno de tus ficheros.
Si trabajas con Python 3, seguramente deberías ver la librería <code>lzma</code> en el módulo <code>tarfile</code>, porque debería abrir ficheros <code>.xz</code> automáticamente. Por ejemplo:
<code>import tarfile
tarfile.open(filename).extractall()
</code>

