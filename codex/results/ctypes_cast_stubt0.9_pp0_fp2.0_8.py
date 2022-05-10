import ctypes
ctypes.cast(struct.fromstring(data_from_db), ctypes.py_object).value
# or
ctypes.cast(struct.fromstring(data_from_db), ctypes.c_char_p).value.decode()
</code>
note: there are many options to get string that stored in DB, mainly depends on type DB and how stores <code>JSON</code>

