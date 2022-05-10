import ctypes
ctypes.cast(id(my_list), ctypes.py_object).value

####################################################################################################
# List Practice
####################################################################################################

# l = ['C']
# for i in range(5):
#     l.append(l[i] + '+')
# print ''.join(l)
# prints C+C++C+++C+++++C+++++++

# l = [1,2,3,4,5]
# st = l[0:5]
# print st
# prints [1,2,3,4,5]
# for i in st[0:3]:
#     st.insert(i,'+')
# print st
# prints [1, '+', 2, '+', 3, '+', 4, '+', 5, '+']

# Name = "Michael Jackson"
# print Name[0]
# print Name[-3]
# print Name[0:4]
# print Name[8:12]
# prints M
#         N
#         Mich
#         Jack

# print Name[::2]
# print Name
