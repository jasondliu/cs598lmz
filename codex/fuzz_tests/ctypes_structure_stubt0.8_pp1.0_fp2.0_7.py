import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 20

ctypes.c_char_p.in_dll(ctypes.cdll.msvcrt, "__mb_cur_max").value = 1
p = S()
p.x = b"\x20\x30\x31\x20"
print(p.x.decode('mbcs'))
# на моей машине исключения не бросается
# но если заменить в коде c_char на c_wchar, то исключение бросается при попытке вызова decode()
</code>

