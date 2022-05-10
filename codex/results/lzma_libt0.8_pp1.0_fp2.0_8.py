import lzma
lzma.LZMAFile(fileobj=ZipFile(file, 'r').open('project/book.json.lzma'))
</code>
(I'll leave it to the reader to figure out how to read the JSON and convert it to the desired output format.)

