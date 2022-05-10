import bz2
bz2.BZ2File(path_to_bz2_file, 'rb')

import gzip
gzip.open(path_to_gzip_file, 'rb')

import lzma
lzma.LZMAFile(path_to_xz_file)
```

## Сериализация и десериализация

Сериализация и десериализация позволяет конвертировать объекты в другие форматы данных, как правило, в файлы. Это полезно, когда данн
