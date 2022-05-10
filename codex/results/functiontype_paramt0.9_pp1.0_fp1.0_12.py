from types import FunctionType
list(FunctionType(sort_func.__code__).__closure__)[0].cell_contents
# the explanation:
# FunctionType(code, globs, name=None, argdefs=None, closure=None)
# Transform a code object to a function object

sort_func.__closure__
sort_func.__code__.__closure__
sort_func.__defaults__
sort_func.__get__(['jkl'].sort, list)


# 这是直接用 lambda 写成的归并排序算法
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return list(merge(left, right))


def merge(left, right):
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
