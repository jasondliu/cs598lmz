import lzma
lzma.LZMAError: Not enough data for header
</code>
I am not sure what is wrong, the file I am trying to save should have been opened with zipfile.ZipFile() so it shouldn't have a header.

