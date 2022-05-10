import lzma
lzma.open('data.xz')
</code>
The issue I am having is that I cannot seem to find a way to directly write the output to the decompressed file without first decompressing it to memory. Here is what I tried:
<code>input_file = lzma.open('data.xz')
output_file = open ('data', 'w+b')
output_file.write(input_file.read())
</code>
The problem with this is that it first decompresses the entire file to memory.
<code>   for data in input_file:
        output_file.write(data)
</code>
This results in the same issue.
<code>with open('data', 'w+b') as outfile:
    shutil.copyfileobj(input_file, outfile)
</code>
This is the only one that doesn't use memory. However, it ends up writing garbage to the file.
<code>shutil.copyfileobj(input_file, output_file)
</code>
This also writes garbage to the file.
<code>for data in input_
