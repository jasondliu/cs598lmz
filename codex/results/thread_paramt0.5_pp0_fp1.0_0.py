import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# #################################################################################################
# Input/Output Input/Output Input/Output Input/Output Input/Output Input/Output Input/Output
# #################################################################################################

# Python3 program to print alphabet pattern 'A'

# * * * * * * * *
# *             *
# *             *
# * * * * * * * *
# *             *
# *             *
# * * * * * * * *
#
# size = 7
#
# # Function to demonstrate printing pattern
# def alphabet_pattern(size):
#     # Initialize pattern
#     pattern = []
#     for i in range(0, size):
#         row = []
#         for j in range(0, size):
#             row.append(' ')
#         pattern.append(row)
#
#     # Fill the pattern
#     for i in range(0, size):
#         for j in range(0, size):
#             if i == 0 or i == size // 2 or i == size - 1 or j == 0
