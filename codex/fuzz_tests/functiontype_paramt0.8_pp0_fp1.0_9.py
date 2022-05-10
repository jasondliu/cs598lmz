from types import FunctionType
list(FunctionType(lambda x, y: x + y, globals(), {}))

# String
list("Romeo, wherefore art thou?")
list("The quick brown fox jumps over the lazy dog")

# Tuple
list((1, 2, 3, 4))
list(("python", "django", "flask"))
list((True, False))
list((50,))

# Set
list({"a", "b", "c", "d"})
list({True, False})
list({50, 25, 14, 51, 17, 22})

# Dictionary
list({1: "a", 2: "b", 3: "c"})
list({"name": "Oscar", "last_name": "Ortiz", "age": 21})

# Range
list(range(0, 10))
list(range(10))
list(range(0, -10))

# Other iterable objects
sf_temps = [82, 85, 88, 100, 110]
list(enumerate(sf_temps, start=1))
list(reversed(sf
