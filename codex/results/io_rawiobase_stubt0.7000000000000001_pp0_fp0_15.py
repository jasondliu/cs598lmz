import io
class File(io.RawIOBase):
    ...
    def close(self):
        # close underlying file descriptor
        os.close(self.fd)
```

**Important**: the method `close()` is **not** called **automatically** when the file object is garbage collected.

### `file.closefd`

`file.closefd()` closes the file descriptor that this file object wraps.

## File Object Attributes

`file` object attributes:

- `file.closed`
- `file.mode`
- `file.name`
- `file.encoding`
- `file.newlines`
- `file.softspace`

### `file.closed`

`file.closed` is a Boolean indicating whether the file has been closed.

### `file.mode`

`file.mode` is the I/O mode for the file object.

### `file.name`

`file.name` is the name of the file.

**Note**: even though the file object provides a `name` attribute, this is not accurate in all cases (e.g. `sys.std
