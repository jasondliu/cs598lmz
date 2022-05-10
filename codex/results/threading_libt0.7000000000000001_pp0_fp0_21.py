import threading
threading.Thread(target=f).start()
print('END')

# Mutable type
# a = [[]]
# a[0].append(1)
# print(a)

# Immutable type
# a = (1,)
# b = a
# a += (2,)
# print(a, b)

# Immutable type
# a = (1,)
# b = a
# a = a + (2,)
# print(a, b)
