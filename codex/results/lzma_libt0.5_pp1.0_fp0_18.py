import lzma
lzma.decompress(open("../../data/compressed/train.csv.xz", "rb").read())

# The following code is used to create the compressed version of the train.csv
# import lzma
# compressed = lzma.compress(open("../../data/train.csv", "rb").read())
# open("../../data/compressed/train.csv.xz", "wb").write(compressed)

# The following code is used to create the compressed version of the test.csv
# import lzma
# compressed = lzma.compress(open("../../data/test.csv", "rb").read())
# open("../../data/compressed/test.csv.xz", "wb").write(compressed)

# The following code is used to create the compressed version of the sample_submission.csv
# import lzma
# compressed = lzma.compress(open("../../data/sample_submission.csv", "rb").read())
# open("../../data/compressed/sample_submission.csv.xz
