import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello ")).start()
threading.Thread(target=lambda: sys.stdout.write("world\n")).start()

# What's the output?
# A. Hello world
# B. Hello
# C. world
# D. worldHello
# E. can't tell

# Answer: C
# Explanation:
# The threads are started, but they don't wait for each other.
# Therefore, they print their output in the order they are started, not in the order they are written.
# Note: the output might be different on different machines, because the threads might start in different orders.
# On my machine, I got worldHello, but on a different machine, I got worldHello.
# Therefore, the answer is D.
#
#
#
# Question 8:
# What's the output?
#
# def func(lst):
#     lst = [4, 5, 6]
#
# lst = [1, 2, 3]
# func(lst)
# print(lst)
#
# A. [4, 5
