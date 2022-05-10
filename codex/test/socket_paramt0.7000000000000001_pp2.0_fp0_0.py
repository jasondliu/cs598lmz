import socket
socket.if_indextoname('1')

#%% bash

#!cmd
#!cmd arg1 arg2
#!cmd arg1 "arg2 with spaces"
#!cmd arg1 'arg2 with spaces'
#!cmd arg1 arg2 arg3 | grep arg2
#!cmd arg1 arg2 arg3 > file
#!cmd arg1 arg2 arg3 >> file
#!cmd arg1 arg2 arg3 | grep arg2 > file
#!cmd arg1 arg2 arg3 | grep arg2 >> file

#%%

#!cat example.py

#%%

#!python example.py

#%%

#!echo $?

#%%

#!python example.py
#!echo $?

#%%

#!python example.py > out.txt
#!cat out.txt

#%%

#!python example.py | grep 2 > out.txt
#!cat out.txt

#%%

#!python example.py 2> err.txt
#!cat err.txt

#%%

#!python example.py > out.
