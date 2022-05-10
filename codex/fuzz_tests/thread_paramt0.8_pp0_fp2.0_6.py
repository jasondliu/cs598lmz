import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,101)))).start()


# let's go back to the task of combining the values of two dictionaries. We want to make a new dictionary that contains all the keys from dictionary a and b, and if they share
# the same key, we want the value from a. In this case, we can use the update() method of dictionarys, which overwrites values of the same key in the target dictionary
# The update() method changes the dictionary in place, so it returns none
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
print(mergeDict(a,b))


dictA = {'letterA': 'a', 'letterB': 'b', 'letterC': 'c'}
dictB = {'letterD': 'd', 'letterE': 'e', 'letterF': 'f'}
def mergeDict(a, b):
    return
