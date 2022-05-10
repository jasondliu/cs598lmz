from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# %% [markdown]
# #### Exercise 10.1:
# Write a function that reads an entire file into a string, with a better error message if the file doesn't exist.

# %%
def read_file(file_name):
    """
    reads a file and returns it as a string.
    If the file doesn't exist, the function returns a better error message
    """
    try:
        with open(file_name) as blob:
            return blob.read()
    except FileNotFoundError:
        print(f"Sorry, {file_name} isn't available.")


# %%
# test the function
print(read_file('alice.txt'))
print(read_file('ghost.txt'))

# %% [markdown]
# #### Exercise 10.2:
# Write a function that takes a filename, a word and a string as arguments and replaces the word with the string in the file.
#
#

# %%
def replace_word_in_file(file_name, word, new_word):
    """
