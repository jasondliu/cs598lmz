import ctypes
ctypes.cast(matrix, ctypes.py_object).value

for i in range(1, rows):
    if matrix[i][0] == 1:
        matrix[i][0] = 0
    else:
        matrix[i][0] = 1


for j in range(1, cols):
    if matrix[0][j] == 1:
        matrix[0][j] = 0
    else:
        matrix[0][j] = 1


for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][j] == 1:
            matrix[i][0] = 0
            matrix[0][j] = 0

for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 1

if first_row_has_zero:
    for j in range(cols):
        matrix[0][j] = 0
if first_col_has_zero
