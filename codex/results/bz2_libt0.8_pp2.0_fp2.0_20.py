import bz2
bz2.decompress(ciphered)

# But you can also import the entire module so you don't have to use the
# prefix:

from bz2 import decompress
decompress(ciphered)

# The same holds true for when you import the entire module:

import pickle
pickle.loads(ciphered)

# Here's an example of how to alias a module:

import bz2 as b
b.decompress(ciphered)

# And here's an example of how to alias a class:

from pickle import loads as load
load(ciphered)

# Now that we've shown how to import modules and classes, let's show how to
# use them to build a basic computer program.

# Hangman

# In this problem, we'll implement a simple version of the classic word game
# Hangman, which we will play against the computer.

# The computer will pick a random word, and you will guess the word one
# character at a time. If you guess correctly, the character will appear in
# its correct location in the word.
