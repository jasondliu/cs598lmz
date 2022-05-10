import lzma
lzma.LZMAError: Not enough data for stream header
</code>
I'm trying to open an .xz file that I zipped on an Ubuntu box and am trying to unzip on a Mac. I can't figure out what I'm doing wrong.
The input file is here.
Thanks in advance!


A:

Use this instead:
<code>with lzma.open("./pagelinks.xz", "rb") as xzfile:
    with open("./pagelinks", "wb") as pagelinks:
        pagelinks.write(xzfile.read())
</code>

