from types import FunctionType
list(FunctionType(f, globals()) for f in [lambda x:x, lambda x:x*2, lambda x:x*3])

#lambda和map/reduce：一直认为map和reduce不好用，拒绝使用，但是学习到现在，真的得承认jython当中的map和reduce是挺好用的，只是我理解的方式不对
list(map(lambda n: n+1, [1,2])) #[2, 3]
list(map(lambda s: s.upper(), ['Hello','World'])) #['HELLO', 'WORLD']
list(map(lambda s: s.replace('l','x'), "Hello,World".split(','))) #['Hexxo', 'Worxd']
list(map(lambda s, t:s*t, [1,2], [100,200
