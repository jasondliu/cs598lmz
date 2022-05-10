import ctypes
# Test ctypes.CFUNCTYPE 
def call_callback(f, arg):
    print(arg)

callback_type = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

instance = callback_type(call_callback)
instance(' This is a message!')
</code>
Output:
<code>b' This is a message!'
</code>
I want to break down the complete process as following

Create a function "call_callback" and use decorator "@ctypes.CFUNCTYPE" 
to convert the function to a callback function
Assign a value to "arg" the argument of "call_callback"
In the next step, call the callback function with argument defined in
the previous step "instance(arg)"

This process should work, but this throw an error: 
<code>TypeError: call_callback() takes exactly 2 arguments (1 given)
</code>
My question is that do I miss any step in the process of invoking callback function?
Or any other mistake?
Thanks.


A:

Your description of the process doesn't line up with the code
1
