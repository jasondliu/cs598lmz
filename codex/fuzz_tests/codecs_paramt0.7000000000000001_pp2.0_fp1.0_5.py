import codecs
codecs.register_error('strict', codecs.replace_errors)
s = u'\ud800\udc0a'
s.encode("ascii", "strict")

# m = {}
# for i in [1,2,3]:
#     if i not in m:
#         m[i] = 1
#     else:
#         m[i] += 1
# m

# {: 2d}
"{: 2d}".format(5)
"{: 2d}".format(50)

#
# nums = [1,2,3]
# nums.reverse()
# nums
# nums.sort()
# nums

# [i for i in range(10)]
# [i for i in range(10) if i%2 == 0]
# [i for i in range(10) if i%2 == 1]
# [i for i in range(10) if i > 4]

# def foo():
#     abc = 10
#     def bar():
#         nonlocal abc
#         abc =
