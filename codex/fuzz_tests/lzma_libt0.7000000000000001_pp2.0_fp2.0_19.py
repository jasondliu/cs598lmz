import lzma
lzmaFile = lzma.open('/Users/kazuki/Downloads/train_f.csv.xz')

train_f = pd.read_csv(lzmaFile)

del train_f['ID_code']
del train_f['target']
gc.collect()

train_f.head()


# In[ ]:


train_f.columns = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','f22','f23','f24','f25','f26','f27','f28','f29','f30','f31','f32','f33','f34','f35','f36','f37','f38','f39','f40','f41','f42','f43','f44','f45','f46','f47','f48','f49','f50','f51','f52','f53','f
