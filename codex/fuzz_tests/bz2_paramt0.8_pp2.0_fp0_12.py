from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# numpy.savez 存取多个数组
np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
arch['b']

# numpy.savez_compressed 压缩存储
np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)

# 使用 pandas 存储数据
frame = pd.Dataframe({'a':np.random.randn(100),
                      'b':['foo','bar']*50,
                      'c':np.random.randn(100)})
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']

frame.to_hdf('mydata.h5', 'obj3', format='table')

store.put('obj2',
