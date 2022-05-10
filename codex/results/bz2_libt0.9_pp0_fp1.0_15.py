import bz2
bz2.decompress(x)

exit()

iter = 0
for k in range(10000):
    z = zeros_like(x)
    z = z.reshape(3,3153)
    iter += 1
    print iter

# while 1:
#     iter += 1
#     if iter % 1000 == 0:
#         print iter
#     t = m(x)
#     if t == [6, 13, 9, 14, 14, 10, 9, 12, 10]:
#         quit()
#     x += 1
#     # print t
#
# a = [5, 9, 4, 10, 5, 9, 12, 3, 5]
# b = array([5, 9, 4, 10, 5, 9, 12, 3, 5])
# print m(b)
#
# def mmm(x):
#     y = [0 for i in range(256)]
#     for i in x:
#         y[i] += 1
#     return y
#
# print mmm(a)

#print 2580*
