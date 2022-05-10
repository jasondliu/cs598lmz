import selection_sort
import quick_sort
import merge_sort
import shell_sort
import bucket_sort
import counting_sort
import radix_sort
import heap_sort

# Test data
A = np.random.randint(0, 100, 20)
print('Initial Test Data:')
print(A)

# 1. Bubble Sort
print('\nBubble Sort:')
Bubble_Sort = bubble_sort.bubbleSort(A)
print(Bubble_Sort)

# 2. Insertion Sort
print('\nInsertion Sort:')
Insertion_Sort = insertion_sort.insertionSort(A)
print(Insertion_Sort)

# 3. Selection Sort
print('\nSelection Sort:')
Selection_Sort = selection_sort.selectionSort(A)
print(Selection_Sort)

# 4. Quick Sort
print('\nQuick Sort:')
Quick_Sort = quick_sort.quickSort(A, 0, 19)
