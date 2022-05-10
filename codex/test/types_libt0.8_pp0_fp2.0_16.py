import types
types.NoneType

# None is an object

type(None)

# None is a singleton
a = None
b = None
a is b

# None is falsy
bool(None)

# None is not a string
str(None)

# None is not an integer
int(None)

# None is not a float
float(None)

# -------------------------------------------------
# NoneType
# -------------------------------------------------

a = None
type(a)
dir(a)


# -------------------------------------------------
# NoneType doesn't have any methods or attributes
# -------------------------------------------------

# a.lower()

# a.capitalize()

# a.upper()

# a.title()

# a.format()

# a.replace()

# a.index()

# a.strip()

# a.isalnum()

# a.startswith()

# a.endswith()

# a.isdigit()

# a.isalpha()

# a.isupper()

# a.islower()

