import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Day 3: Squares With Three Sides")

# Read file
file = open('day3inputs.txt', 'r')
inputs = file.read().splitlines()
file.close()

# Vars
valid_triangles = 0

# Find number of valid triangles
for i in range(0, len(inputs)):
    # Create triangle
    triangle = [int(x) for x in inputs[i].split()]

    # Sort
    triangle.sort()

    # Check triangle
    if (triangle[0] + triangle[1]) > triangle[2]:
        valid_triangles += 1

# Print
print("Valid triangles: " + str(valid_triangles))
