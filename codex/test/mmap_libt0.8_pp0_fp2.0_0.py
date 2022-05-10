import mmap

def matrix_to_array(matrix):
    arr = []
    for row in matrix:
        for element in row:
            arr.append(element)
    return arr

# TODO: remove hard-coded values for N,N1,N2
def save_matrix_to_file_mmap(matrix, file_path):
    arr = matrix_to_array(matrix)
    arr = array.array('L', arr)
    f = open(file_path, 'wb+')
    f.write(arr)
    f.close()

# TODO: remove hard-coded values for N, N1, N2
def load_matrix_from_file_mmap(file_path):
    matrix = []
    f = open(file_path, 'rb+')
    arr = array.array('L')
    arr.fromfile(f, 1024)
    for i in range(0,32):
        matrix.append([0] * 32)
