import lzma
# Test LZMADecompressor Object
# it does not support context manager (__enter__, __exit__ methods)
ld = lzma.LZMADecompressor()

with open("enwik8", "rb") as f:
    f_contents = f.read()
    res = ld.decompress(f_contents) 
    print(res[:100])
    print("Type res: ", type(res))
    print("Length res: ", len(res))

# with open("enwik8", "rb") as f:
#     with lzm.open(f) as lzf:
#         contents = lzf.read()
#         print("Type Contents: ", type(contents))
#         print("Length Contents: ", len(contents))
#         print("contents: ", contents)

# # Test LZMAFile Object

# # LZMAFile has better documentation pages, not sure what is the difference for these 2 object.


# # suppose we have a file named "foo", it consists of one line.

# with open("foo", "w
