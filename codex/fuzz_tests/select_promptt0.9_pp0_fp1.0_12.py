import select
# Test select.select
print select.select([],[],[])
# ---------------------------------

# ----------------------------
# Test select.select in a loop
data = 'aQWERTY'
r = select.select([sys.stdin], [], [], 5) #this will block until input on sys.stdin, or until 5 seconds have passed
print r
dataIn = r[0][0].read()
print data == dataIn
# ---------------------------------

# #--------------
# import sys
# import select
# print select.select([],[sys.stdout],[])
# # # ----------------------------
# # import sys
# # import select
# # data = 'aQWERTY'
# # select.select([],[sys.stdout], [], 5)
# # sys.stdout.write(data)
# # sys.stdout.flush()
#--------------
