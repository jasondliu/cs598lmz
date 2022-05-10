import bz2
bz2_file = bz2.BZ2File('books/book.bz2')
bz2_file.read()

# there are many other compression libraries including: lzma, gzip, zip and snappy
# snappy is a Google compression library
# luckily, there is a python module called 'python-snappy'
# http://pythonhosted.org/python-snappy/

# Exercise 18

# you can use the 'requests' library to download files from the internet
# http://docs.python-requests.org/en/latest/user/quickstart/

# using requests, download the following file:
# https://s3.amazonaws.com/thedataincubator/coursedata/mldata/train.csv.bz2

# the file is compressed with bz2, so you'll need to decompress it
# before you can use it

# once you have done this, you'll have a file called 'train.csv'
# which is a spreadsheet of training examples for a machine learning
# problem
# each row in the file corresponds to
