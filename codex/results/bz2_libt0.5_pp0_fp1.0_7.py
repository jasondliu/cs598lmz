import bz2
bz2.BZ2File('data/example4.bz2')

# %%
# Для сериализации данных в формате HDF5 существует пакет h5py.
# Он предоставляет доступ к данным в формате HDF5 из питона.
import h5py
f = h5py.File('data/mydata.h5', 'w')

# %%
# Создаем группу в файле.
group = f.create_group('subgroup')

# %%
# Создаем датасет.
dset = f.create_dataset('subgroup/
