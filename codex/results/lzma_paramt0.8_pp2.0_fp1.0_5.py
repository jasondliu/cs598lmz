from lzma import LZMADecompressor
LZMADecompressor().decompress(open("tmp.tar.xz", "rb").read()) 

print("Extracting tar archive....")
tf = tarfile.open("tmp.tar")
tf.extractall("/tmp/usr")
tf.close()

print("Done.")
