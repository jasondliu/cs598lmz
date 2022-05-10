from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("test.bz2", "rb").read())

#bz2.BZ2File("test.bz2").read()

#bz2.decompress(open("test.bz2", "rb").read())

#bz2.decompress(open("test.bz2", "rb").read().decode("utf-8"))

#bz2.decompress(open("test.bz2", "rb").read().decode("utf-8").encode("utf-8"))

#bz2.decompress(open("test.bz2", "rb").read().decode("utf-8").encode("utf-8")).decode("utf-8")

#bz2.decompress(open("test.bz2", "rb").read().decode("utf-8").encode("utf-8")).decode("utf-8").encode("utf-8")

#bz2.decompress(open("test.bz2", "rb").read().decode
