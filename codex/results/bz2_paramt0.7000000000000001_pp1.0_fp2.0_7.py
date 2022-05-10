from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressedData)

# 
# Problem 2
#
def generateHuffmanTree(chars):
    """
    Generate a Huffman tree for chars with frequencies,
    and return a dictionary mapping symbols to binary codes.
    """
    assert type(chars) == type({}), "chars is not a dictionary"
    # Base case of recursion:
    #   One element in chars, all symbols have frequency 1.
    if len(chars) == 1:
        (char, freq) = chars.popitem()
        return {char: "0"}
    # Find two characters with lowest frequencies.
    if chars:
        x = min(chars.iteritems(), key=lambda (c,f):f)[0]
        del chars[x]
    if chars:
        y = min(chars.iteritems(), key=lambda (c,f):f)[0]
        del chars[y]
    else:
        return None
    # Create a branch with these two nodes.
    chars[(x,y)] = chars.get(x
