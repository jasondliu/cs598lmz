import types
types.MethodType(m,None)            ## method object
types.MethodType(m,n)               ## bound method object
 
#----------------------------------------------------------------------------#
#                                                                            #
#                               for 循环语句                                  #
#                                                                            #
#----------------------------------------------------------------------------#

for i in [1,2,3]:
    print i
    
for c in 'Hello World':
    print c

for i in range(10):
    print i

for i in range(5):
    print i;
    
for i in range(5): print i;  ## One line for statement.

#----------------------------------------------------------------------------#
#                                                                            #
#                               while 循环语句                                #
#                                                                            #
#----------------------------------------------------------------------------#

i = 0
while i < 10:
    print i
    i = i + 1
    
#----------------------------------------------------------------------------#
#                                                                            #
#                            Python条件语句和循环语
