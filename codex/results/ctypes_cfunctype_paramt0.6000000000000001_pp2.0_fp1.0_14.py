import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def my_callback():
    print('callback')

callback_type = FUNTYPE(my_callback)
</code>
I want to pass this callback_type to my C code.
<code>void call_me(void (*f)(void)){
    f();
}
</code>
But I don't know how to do it.
I tried this:
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(None)

def my_callback():
    print('callback')

callback_type = FUNTYPE(my_callback)

lib = ctypes.CDLL('./lib.so')

lib.call_me(callback_type)
</code>
But I have this error:
<blockquote>
<p>Traceback (most recent call last):   File "test.py", line 15, in
  
      lib.call_me(callback_type) TypeError: byref() argument must be a ctypes instance</p>
</blockquote>


A:

<code>ctypes.CFUNCT
