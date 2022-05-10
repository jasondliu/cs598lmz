from lzma import LZMADecompressor
LZMADecompressor().decompress("...")
LZMADecompressor().flush()
"""
input_file = "trained_qa_model.tf"
with gzip.open("","rb") as input_file:
    file_content = input_file.read()

with open("", "wb") as output_file:
    output_file.write(file_content)


# print("hello python world")
# print("hello, \"PYTHON\"")
# print("hello" + "python")
# str = "python_programming"
# print("hello, %5.5s world!" % str)
# """
# year = 2017
# month = "11th"
# day = "08"
# print("{0}년 {1}일 {2}".format(year, month, day))
# # print("%d년 %s일 %s" % (year, month, day))
# print("{0:>8}".format(169))
# print("{0:0>8}".format(169))
#
# print
