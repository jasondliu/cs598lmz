import types
types.new_class('complex')

complex(1, 2)
# (1 + 2i)

complex('3+5j')
# (3 + 5j)

complex(1,2) + complex(3,5)
# (4 + 7j)

(1+2j) * (3+5j)
# (-7 + 11j)
