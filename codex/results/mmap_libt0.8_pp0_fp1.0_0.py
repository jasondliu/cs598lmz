import mmap

def checkList(array, p):
    # move to next index, then check.
    if array[p + 1] != -1:
        return array[p + 1] - 1 
    if array[p + 2] != -1:
        return array[p + 2] - 1
    if array[p + 3] != -1:
        return array[p + 3] - 1
    if array[p + 4] != -1:
        return array[p + 4] - 1
    if array[p + 5] != -1:
        return array[p + 5] - 1
    if array[p + 6] != -1:
        return array[p + 6] - 1
    if array[p + 7] != -1:
        return array[p + 7] - 1
    if array[p + 8] != -1:
        return array[p + 8] - 1
    if array[p + 9] != -1:
        return array[p + 9] - 1
    if array[p + 10] != -1:
        return array
