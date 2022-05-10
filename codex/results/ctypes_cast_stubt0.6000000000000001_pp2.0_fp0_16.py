import ctypes
ctypes.cast(p, ctypes.c_char_p).value

# Get the length of the message
ctypes.cast(ctypes.c_char_p(p), ctypes.POINTER(ctypes.c_size_t)).contents.value

# Free the memory
ctypes.CDLL('libc.so.6').free(p)
```

## License

MIT.
