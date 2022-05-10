import lzma
lzma.decompress(bytes(lzma_data))

#%%
import pickle
pickle_data = pickle.dumps(data)
print(pickle_data)

#%%
data = pickle.loads(pickle_data)
print(data)
