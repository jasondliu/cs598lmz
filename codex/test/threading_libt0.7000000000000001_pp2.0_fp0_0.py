import threading
threading.stack_size(67108864)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(merge_sort(left))
    if len(right) > 0:
        result.extend(merge_sort(right))
    return result

arr = []
for i in range(10000):
    arr.append(random.randint(0,10000))

print(merge_sort(arr))
