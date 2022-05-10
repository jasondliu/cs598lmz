import types
types.MethodType(__import__('B'), 'C')

# __import__('B')
# B.__import__('B')

# __import__('B')
# __import__('C')
# __import__('C')
# C.__import__('B')
# C.__import__('C')

# __import__('C')
# __import__('C')
# __import__('B')
# __import__('B')
# __import__('C')
# __import__('C')

# __import__('B')
# __import__('C')
# __import__('B')
# __import__('C')

# __import__('B')
# __import__('B')
# __import__('C')
# __import__('C')
