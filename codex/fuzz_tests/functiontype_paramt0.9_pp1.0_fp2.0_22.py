from types import FunctionType
list(FunctionType(20, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',\
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',\
 'y', 'z', 'aa'))

#Comparisons
a = 0
while a < 5:
    print(a)
    a = a + 1

list('abcdefghijklmnopqrstuvwxyz')[25]

#Finding the index of a var in a list of vars
def GetIndexInList(var, list):
    if var in list:
        return list.index(var)
    return -1

#Index of the first var in the argument list

#Finding the index of an element in an array
def FindIndex(Array, ElementToFind):
    for x in range(0, len(Array)):
        if ElementToFind != Array[x]:
            return x
    return -1

