import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)
dll.add_a_callback(FUNTYPE(callback))
dll.get_a_callback()
```

```c++
void callback(int n, const char* s)
{
    std::cout << n << std::endl;
    std::cout << s << std::endl;
    std::cout << "Hello from C++ via callback!" << std::endl;
}
```

```python
def callback(n, s):
    print(n)
    print(s)
    print("Hello from Python via callback!")
```
