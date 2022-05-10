from types import FunctionType
list(FunctionType(lambda a: a*2, globals(), 'dbl'))

#list(map(lambda a: a*2, [1,2,3]))

#list(filter(lambda a: a%2 == 0, [1,2,3,4,5]))

#list(map(lambda a: a*2, filter(lambda a: a%2 == 0, [1,2,3,4,5])))

#print(any(['a', 'b', 'c']))
#print(any(['a', 'b', '']))
#print(all(['a', 'b', 'c']))
#print(all(['a', 'b', '']))

#print(any([0,1,2]))
#print(any([0,0,1]))
#print(all([0,1,2]))
#print(all([0,0,1]))

#print(any(('a', 'b', 'c')))
#print(any(('a', 'b', '')))
#print(all(
