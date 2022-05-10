from types import FunctionType
list(FunctionType(lambda x: x+1, {}, None, None, None).__code__.co_consts)

# 3. How do you move a file in Python?
import os
os.rename('old_name.txt', 'new_name.txt')

# 4. How do you get the last element of a list?
my_list = [1, 2, 3, 4]
my_list[-1]

# 5. Why should you not modify a list while iterating it?
# because it is not guaranteed to work.

# 6. How can you copy a list?
# using slice
new_list = my_list[:]

# 7. What is the difference between range and xrange?
# range() is equivalent to xrange() except it does not return an xrange object
# but creates a list instead.

# 8. How do you remove the last element of a list?
my_list.pop()

# 9. How do you remove the first element of a list?
my_list.pop(0)

# 10. What exception is raised when the user enters invalid
