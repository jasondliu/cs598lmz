import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = np.array([1,2,3,4,5])
y = np.array([6,7,2,8,4])

#%%
# 数组比较
print(x == y)
print(np.array_equal(x,y))

#%%
# numpy中的排序
arr = np.array([3,2,0,1])
print(np.sort(arr))

#%%
# 数组排序
arr = np.array([[3,2,4],[5,0,1]])
print(np.sort(arr))
print(np.sort(arr, axis = 0))
print(np.sort(arr, axis = 1))

#%%
# 排序算法
values = np.array([5,0,1,3,2])
indexer = values.argsort()
print(indexer)
print(values[indexer
