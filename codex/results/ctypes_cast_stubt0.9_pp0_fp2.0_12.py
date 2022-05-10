import ctypes
ctypes.cast(222, ctypes.c_float)
 
# ValueError: cast() arg 2 must be a pointer, not float
```

`ctypes`는 파이썬 프로그램에서 외부 라이브러리를 호출하게합니다.  

### [5.49.3 `ctypes`로 외부 라이브러리 호출](https://dojang.io/mod/page/view.php?id=2485)

프로그램에서 외부 C 라이브러리를 호출할 때는 `CDLL` 클래스 혹은 `
