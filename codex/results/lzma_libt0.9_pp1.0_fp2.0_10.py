import lzma
lzma_dict = {
    'COPY_GPL': lzma.open('./COPYING.txt.xz'),
    'COPY_LGPL': lzma.open('./COPYING.LGPL.txt.xz'),
    'COPY_QPL': lzma.open('./COPYING.QPL.txt.xz')
}

# Ugly quick sort (plz don't throw things at me!)
# This is what happen when you procrastinate xD

def quickSort(lst):
    n = len(lst)

    # fixing the lists
    if n <= 2:
        if n == 2:
            if lst[0].name > lst[1].name:
                t = lst[0]
                lst[0] = lst[1]
                lst[1] = t
        return lst

    # doing the sorting
    pivot = lst[0].name
    smaller = []
    equal = []
    bigger = []

    for i in lst:

