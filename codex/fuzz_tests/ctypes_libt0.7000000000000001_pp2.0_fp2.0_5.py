import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# Write a function that takes in a number and a list of numbers. It should return
# a new list with the elements of the input list shuffled.

def shuffle(a, list):
    real_list = ""
    while len(list) != 0:
        rand_num = random.randint(0, a - 1)
        real_list += list[rand_num]
        list.pop(rand_num)
    return real_list


def num_to_list(a):
    list = []
    for i in range(a):
        list.append(str(i))
    return list


def list_to_str(list):
    str = ""
    for i in list:
        str += i
    return str


# print(list_to_str(shuffle(10, num_to_list(10))))

# Write a function that returns the largest element in a list.

def find_largest(list):
    largest = list[0]
