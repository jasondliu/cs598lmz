import ctypes
ctypes.cast(test, id(test))
</code>
I am getting the output as None.
In C the same can be achieved using (void*) typecasting. I am just trying to understand how can i do this in python.
The reason why i am trying to do this is because i am trying to implement some pipe based IPC communication. I am using named pipes and need to use some form of message queuing in my program. I want to pass the address of the python object, which stores the pipe name, from one program to another.
Any suggestions?
Thanks.


A:

Just a hunch, but I think pty uses <code>curses</code>, which is precompiled for your machine's specific word size, so the python code would have to guess at it.
Someone else had this problem with a different python-extension and wrote a ctypes override for it that worked for them. Note that he got the word size wrong :)
Anyway, hopefully this will give you a starting point.

