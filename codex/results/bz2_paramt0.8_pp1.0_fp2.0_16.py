from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(message)
</code>
How can I catch this error? What does this error mean?


A:

I went through the same pain.
The problem is not in the exception handling. The problem is within the bytes object you are passing as the parameter.
When you fetch the data from the CSV file and put it into a bytes object you play with the encoding options.
You may have used utf-8.
But while decompressing you should use bytearrays.
Remove any encoding stuff and use the bytes object directly.

