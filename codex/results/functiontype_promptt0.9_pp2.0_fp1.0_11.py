import types
# Test types.FunctionType to see if the object passed is a *function*.

def applyToEach(L, f):
    '''
    Assumes that
    L is a list, f a function
    Mutates L by replacing each element, e, of L by f(e)
    '''
    for i in range(len(L)):
        L[i] = f(L[i])


def printList(L):
    '''
    Assumes that L is a list of integers
    Prints the value of L.
    '''
    for i in L:
        print(int(i))


testList = [1, -4, 8, -9]
applyToEach(testList, abs)

print('')

printList(testList)
