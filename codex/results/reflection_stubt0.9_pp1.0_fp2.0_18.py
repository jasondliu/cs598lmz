fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test'
print(fn)


# str_test = "%d + %d = %d"
# print(str_test % (1, 2, 5))

# a = [1, 2, 3, 4]
# print(a.__class__)
# print(dir(a))
# print(id(a))
# print(hash(a))
# a[3] = 5
# print(a)
# str1 = "hello"
# str2 = "world"
# print(str1 + str2)

# a = (1, 8, [8, 9])
# print(hash(a))
# a[2][0] = 888
# print(hash(a))

# d = {'112': 2}
# print(d.__class__)
# print(d['112'])
# print(d['113'])
# a = [1, 2]
# print(id(a))
# a.append(3)
# print(a)
# print
