import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
compressor.decompress(b"")

with open("tests/input.txt", "r") as input:
    comp = lzma.compress(input.read().encode("utf-8"))
    decomp = compressor.decompress(comp)

assert decomp == "Lorem ipsum ad his scripta blandit partiendo, eum fastidii accumsan euripidis in, eum liber hendrerit an. Qui ut wisi vocibus suscipiantur, quo dicit ridens inciderint id. Quo mundi lobortis reformidans eu, legimus senserit definitionem ex has. Eu sit tincidunt incorrupte definitionem, vis mutat affert percipit cu, eirmod consectetuer signiferumque eu per. In usu latine equidem dolores. Quo no falli viris intellegam, ut fugit veritus placerat per."

# Test LZMACompressor
compressor = lzma.
