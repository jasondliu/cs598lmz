import threading
threading.Thread(target=file_read, args=(file_path,)).start()
help(unicodedata.normalize)
my_list = list(range(0, 80))
print(my_list)
my_list.reverse()
print(my_list)
my_list.remove(0)
print(my_list)
my_list.append(100)
print(my_list)

string_list = list("shinobi")
print(string_list)

print(type(string_list))

print(string_list[0], string_list[2], string_list[-2])

print(string_list[0:4], string_list[:4], string_list[0:],string_list[::-1])

print(string_list[:-1])

string_list.insert(4, '_')
print(string_list)

string_list.insert(0, '_')
print(string_list)

string_list.insert(len(string_list), '_')
print(string_list)
