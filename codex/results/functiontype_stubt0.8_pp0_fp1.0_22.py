from types import FunctionType
a = (x for x in [1])
a((y for y in range(3)))

# dtype = {'names':['name','age','chinese','math','english'],
#         'formats':['U32','i','i','i','i']}
# student = np.array([('张飞',16,75,100,90),('关羽',17,85,96,88.5),
#                     ('刘备',17,85,96,88.5),('典韦',16,76,95,84)],
#                    dtype=dtype)
# student.dtype.names
# b = np.array([5,5,5,5])
# # print(np.sum(b,axis=0))
# # print(np.sqrt([4,4,4,4]))
# np.add(student,b,b)
# print(b)
# np.concatenate((student,b.reshape(1,5)))
# print(student)

# def count():
#     fs = []
#     for
