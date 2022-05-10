import ctypes
ctypes.cast(lib.dfs_get_first, ctypes.c_void_p).value
</code>
Выдаёт следующую ошибку:
<code>ValueError: Procedure called with not enough arguments (4 bytes missing) or wrong calling convention
</code>
Описание функции dfs_get_first:
<code>dfs_file_t* dfs_get_first(dfs_file_t* dir, dfs_dir_t* dd)
</code>
Как правильно переписать код, что бы выводилась первая директория?


A:

<code>from ctypes import *

lib = cdll.LoadLibrary('./libdfs.so')
lib.df
