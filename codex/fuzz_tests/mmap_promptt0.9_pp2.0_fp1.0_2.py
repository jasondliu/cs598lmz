import mmap
# Test mmap.mmap in some way.

# Strings are very similar to lists of characters in Python.
# You can use the slice notation on strings.
print("This is a string"[2:5])  # Notice how slicing works.
print("This is a string"[::2])  # Increase 2 is possible.
# We can use the + operator to attach strings together, or the * to repeat strings.
print("Repeat "*10)
# Strings are immutable, so you cant change them in place.
# S[5] = "x" is a type error.
# You can create a new string using string slices, concatenation and replication as on lists.
# The in/not in operators check for membership.
print("This" in "This is a string")
# String methods can be found in the on-line documentation.
# str.find(str, beg=0, end=len(string))
# Returns the lowest index in the string where substring sub is found within the slice s[beg:end].
# Optional arguments start and end are interpreted as in slice notation.
print("This is a string".find("is"))  #
