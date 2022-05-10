from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# The data is a file in the CPython source code.
# It's a list of all the files in the source code.
#
# The first line is:
#
#    "Modules/lzmamodule.c"
#
# which is the file we're looking at right now!
#
# If you want to see the whole list, uncomment the next line:
#
#    print(text)

# The last line is:
#
#    "Python/ceval.c"
#
# That's the file that contains the eval() and exec() functions.
#
# The challenge here is to find the shortest program that starts as
# Python code, but which ends with the string "Python/ceval.c".
#
# You can assume that the initial code is a prefix of the solution.
# In the example above, the answer would be just:
#
#   LZMADecompressor().decompress(data)
#
# But I used a longer initial code just to make the challenge a bit harder.
