from lzma import LZMADecompressor
LZMADecompressor()

# creating a dictionary
# Look at PyDictionary

# split a string into a list of words

# https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/


def convert(s):
    str1 = ""
    return (str1.join(s))


# Driver code
s = ['a', 'b', 'c', 'd']
print(convert(s))

# check if all the elements are unique

# https://www.geeksforgeeks.org/python-check-if-all-items-in-a-list-are-unique/


def checkUnique(list):
    if len(list) == len(set(list)):
        return "True"
    else:
        return "False"


# Driver code
list = [10, 20, 30, 40, 50]
print(checkUnique(list))

# https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/

# lambda functions can
