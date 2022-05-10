import lzma
lzma.decompress(lcompressed)

#****************************************************************
#5.5 - Iterating over a collection and performing an operation on each element
#****************************************************************

#perform operation on each element of a collection
#can do this with a list comprehension or a generator expression
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
print(', '.join(sorted(name.capitalize() for name in names)))

#generator expressions is more memory efficient
#list comprehension evaluates to a list, creates entire list in memory
#generator expression returns a generator, only yields results on demand

#****************************************************************
#5.6 - 
#****************************************************************
