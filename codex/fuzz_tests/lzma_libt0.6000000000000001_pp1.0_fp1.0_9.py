import lzma
lzma.LZMACompressor(format=lzma.FORMAT_XZ)
```

```
import lzma
lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
```

# importlib

```
import importlib
importlib.import_module("")
```

```
import importlib
importlib.reload(module)
```

```
import importlib
importlib.find_loader(name)
```

```
import importlib
importlib.resources.open_binary(package, resource)
```

```
import importlib
importlib.resources.is_resource(package, resource)
```

```
import importlib
importlib.resources.contents(package)
```

```
import importlib
importlib.resources.path(package, resource)
```

```
import importlib
importlib.resources.read_binary(package, resource)
```

```
import importlib

