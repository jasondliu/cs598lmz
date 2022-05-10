import lzma
lzma_compression_supported = True
compressDecompressFunctions = {
                                "deflate_1": (compressDeflate1, decompressDeflate1),
                                "deflate_2": (compressDeflate2, decompressDeflate2),
                                "lzf":      (compressLZF,      decompressLZF),
                                "lzma":     (compressLZMA,     decompressLZMA),
                                "lzo":      (compressLZO,      decompressLZO),
                                "snappy":   (compressSnappy,   decompressSnappy),
                                "zlib":     (compressZLIB,     decompressZLIB)
                              }
compressFunctionNames = compressDecompressFunctions.keys()
compressAlgorithms = {
                        "deflate_1": "zlib deflate level 1",
                        "deflate_2": "zlib deflate level 2",
                        "lzf":      "Lempel-Ziv-Fenwick",
                        "lzma
