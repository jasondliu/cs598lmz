import ctypes
ctypes.cast(0, ctypes.py_object).value

# Read a file and find max line length
max_line_len = 0
with open('file.txt','r') as f:
    for line in f:
        if len(line) > max_line_len:
            max_line_len = len(line)
print(max_line_len)

# Read a file and find max line length (using comprehension)
max([len(line) for line in open('file.txt')])

# Find 2 items in a list that add up to a target value
def find_two_sum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if (complement in nums_map) and (nums_map[complement] != i):
            return (i, nums_map[complement])

# Find 2 items in a list that add up to a target
