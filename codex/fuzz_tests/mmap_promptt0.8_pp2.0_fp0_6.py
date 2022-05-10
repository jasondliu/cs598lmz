import mmap
# Test mmap.mmap
with open(r'C:\Users\szfar\Desktop\Projects\Kaggle\MNIST\train.csv', 'r+') as train_file:
    m = mmap.mmap(train_file.fileno(), 0)
    print(type(m))
    print(type(m[0]))
    print(len(m))
del m

# Test numpy.memmap
# with open(r'C:\Users\szfar\Desktop\Projects\Kaggle\MNIST\train.csv', 'rb') as train_file:
#     buffer = train_file.readlines()
#     print(type(buffer))
#     print(type(buffer[0]))
#     print(len(buffer))

# mm = np.memmap(r'C:\Users\szfar\Desktop\Projects\Kaggle\MNIST\train.csv', dtype='uint8', mode='r', shape=(28, 28, 60000))
# print(type(mm))
# print(type(mm[0]))
# print
