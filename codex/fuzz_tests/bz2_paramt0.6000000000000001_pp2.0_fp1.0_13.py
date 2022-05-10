from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


# 3. Write a Python program to check if a string starts with specified characters.

str1 = input('Enter a string: ')
str2 = input('Enter a string to compare with: ')

def starts_with(str1, str2):
    return str1.startswith(str2)

starts_with(str1, str2)

# In[ ]:


# 4. Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
# https://en.wikipedia.org/wiki/Caesar_cipher

def encrypt(
