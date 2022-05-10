from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = data[mid]
        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            return mid
    return None

print(binary_search(data, b'\x33\x1c\x00\x00'))
print(binary_search(data, b'\x72\x1c\x00\x00'))
print(binary_search(data, b'\x74\x1c\x00\x00'))
print(binary_search(data, b'\x8b\x1c\x00\x00'))
print(binary_search(data, b'\xe7\x1c\x00\x00'))
