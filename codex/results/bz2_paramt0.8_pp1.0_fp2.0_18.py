from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = hacked_decompress

# 16: Write a module that imports and runs
# the double function from the urllib, ftplib, email, and subprocess modules.

# Not doing this because I don't know how to do this.

# 17: Write a function that returns the nth number in the fibonacci sequence.
# http://en.wikipedia.org/wiki/Fibonacci_sequence

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13

# 18: Find a free image hosting site and upload an image. Find the direct URL
# to the image and create an element in your document that uses that URL as
# its src attribute.

# Incorporated this into the index.html file.


