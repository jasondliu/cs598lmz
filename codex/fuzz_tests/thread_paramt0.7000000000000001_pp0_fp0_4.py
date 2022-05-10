import sys, threading
threading.Thread(target=lambda: sys.stdout.write("5\n")).start()
print("6")

# outputs:
# 6
# 5

# Note that not all programs will have the same output. For example, if the program were instead:
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write("5\n")).start()
# sys.stdout.flush()
# print("6")
# then the output might be:
# 5
# 6
# or
# 6
# 5
# or even
# 56
# or some other ordering depending on the threads.

# You will be given a list of N numbers. The ith number in this list represents the number that the program will output at the ith step when run.

# You are required to return a list of all 5-element sublists of this list (including the original list as the only element in a sublist) such that the concatenation of the numbers in the sublist outputs the original list in the order present.

# The elements of the sublists may be in any order.

# For example, given
