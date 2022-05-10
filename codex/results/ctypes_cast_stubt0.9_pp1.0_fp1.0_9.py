import ctypes
ctypes.cast(id(x), ctypes.py_object).value
## object at 0x10079a2d0>
## {...}

def add_record(x, key, value):
    change_protected(x, True)
    x[key] = value
    
    
add_record(x, "new key", "new value")
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
##   File "<stdin>", line 2, in add_record
## TypeError: 'dict' object does not support item assignment

def add_records(x, *updates):
    change_protected(x, True)
    x.update((key, value) 
             for key, value in updates)

add_records(x, ("new key", "new value"))
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
##   File "<stdin>", line 5, in add_records
##   File "<stdin>", line 7, in <gen
