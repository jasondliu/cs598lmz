import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread\n')).start()

#--------------------------------------
# list comprehension for dictionary

# a = [1,2,3]
# b = [4,5,6]
# c = {i:j for i,j in zip(a,b)}
# print(c)

#--------------------------------------
# list comprehension for list

# a = ['a','b','c']
# b = ['1','2','3']
#
# c = [str(i) + str(j) for i,j in zip(a,b)]
# print(c)

#--------------------------------------
# sys.argv[0]

# import sys
# print(sys.argv[0])

#--------------------------------------
# lambda function

# func = lambda x : 2**x
#
# print(func(10))

#--------------------------------------
# if else in one line
# a = 'a'
# b = 'b'
#
# print( 'A' if a == 'a' else 'B' )
# print( 'A' if b
