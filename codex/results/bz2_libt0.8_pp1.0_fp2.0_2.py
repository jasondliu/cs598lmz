import bz2
bz2.compress(b"asdfasdfasdf")

# for x in range(1000):
#     print(x)

# a = [50, 60, 70]
# b = [50, 60, 70]
# b[1] = 54
# b.append(1000)
# b.remove(70)
# b.sort()
# b.reverse()

# b.extend(a)
# # print(b + a)
# print(b)
# print(b.index(70))

a = {1, 2, 3, 4, 4, 5, 6, 4, 4, 4}
a.add(200)
a.remove(4)
a.discard(4)
print(a)

b = {"asdf", "qwer", "zxcv"}
print(type(b))

c = set()
c.add("asdf")
print(type(c))

a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
print(a.
