from lzma import LZMADecompressor
LZMADecompressor.get_uncompressed_data

# get_uncompressed_data is a method that can be used to extract the uncompressed data of an .xz file

with open("data/amazon_reviews_multilingual_US_v1_00.tsv.xz", "rb") as f:
    decompressor = LZMADecompressor()
    file_content = decompressor.decompress(f.read())

# decoding bytes of file read, will return str type

with open("data/amazon_reviews_multilingual_US_v1_00.tsv", "wb") as f:
    f.write(file_content.decode("utf-8"))

# creating a file and writing the string content in it

# creating a pandas dataframe from a file

import pandas as pd
df = pd.read_csv("data/amazon_reviews_multilingual_US_v1_00.tsv", sep="\t")

# splitting a column in a dataframe

import string

# getting the characters

characters = list
