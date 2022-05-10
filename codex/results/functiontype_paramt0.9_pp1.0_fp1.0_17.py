from types import FunctionType
list(FunctionType(None, [1,2,3], None, None, True).__code__.co_varnames)
# ('X','a','t','b',
#  'P','draw','pic','path',
#  'cond','h','g','f','c','d','a2','b2','c2','d2','a1','b1','c1','d1','a0','b0','c0','d0',
#  'a3','b3','c3','d3',
#  'len','point','temp','n','F','i','A',
#  'H','y1','y2','G','x1','x2','first','second','cnt','temp')


set(FunctionType(None, [1,2,3], None, None, True).__code__.co_varnames)
# {'point', 'y2', 'x2', 'P', 'f', 'h', 'i', 'X', 'b1', 'cond', 'F', 'u', 'b2', 'g', 'pic', 'H', 'c1', '
