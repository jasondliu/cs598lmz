import lzma
lzma.decompress(base64.b64decode(content))
</code>
I'm using <code>lzma</code> because the <code>xz</code> library is not available on my server, and I don't have root access to install it.

