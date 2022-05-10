import lzma
# Test LZMADecompressor


def test_decompressor():
    with lzma.open("../data/genomes/genomic_data.fa.lzma") as f:
        result = decompress(f, format="lzma")
    data = _decompress_data("../data/genomes/genomic_data.fa")
    assert result == data


def test_decompress_bytes():
    with lzma.open("../data/genomes/genomic_data.fa.lzma") as f:
        result = decompress(f.read(), format="lzma")
    data = _decompress_data("../data/genomes/genomic_data.fa")
    assert result == data


def test_decompress_decompressor_bytes():
    with lzma.open("../data/genomes/genomic_data.fa.lzma") as f:
        lzc = lzma.LZMADecompressor()
        result = decompress(lzc, f.read(), format="lzma")
    data
