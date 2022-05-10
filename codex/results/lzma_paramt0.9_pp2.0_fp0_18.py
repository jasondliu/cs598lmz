from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor


from appcode.mri.ktrans.cli import parse_args, main
parse_args = parse_args
main = main


# Module implementation
# ======================================================================
class PythonLzmaDecompressor(LZMADecompressor):
    def decompress(self, data, max_length=None, *args, **kwargs):
        output = io.BytesIO()
        with io.BytesIO(data) as lzma_file:
            lzma_decomp = py_lzma.LZMADecompressor()
            while True:
                chunk = lzma_file.read(SETTINGS.BUFFER_SIZE)
                if not chunk:
                    break
                output.write(lzma_decomp.decompress(chunk))
        return output.getvalue()


def lzma_decompress(data):
    return LZMADecompressor().decompress(data)


def load(filename):
    return pickle.load(open(filename, 'rb'))


