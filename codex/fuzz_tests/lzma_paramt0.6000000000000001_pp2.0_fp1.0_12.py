from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

### lzma.LZMACompressor

```python
class lzma.LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)
```

`LZMACompressor` instances can be used to compress data incrementally.

*   `format` – The container format to use for the output. This can be one of the predefined constants `FORMAT_XZ`, `FORMAT_ALONE`, `FORMAT_RAW` or a custom format created with `lzma.FORMAT_RAW` or `lzma.FORMAT_XZ`.
*   `check` – The integrity check to use. This can be one of the predefined constants `CHECK_NONE`, `CHECK_CRC32`, `CHECK_CRC64`, `CHECK_SHA256` or a custom check value.
*   `preset` – The compression preset to use. This can be an integer in the range from `0` to `9`, or `None` for the default preset.
*   `filters` –
