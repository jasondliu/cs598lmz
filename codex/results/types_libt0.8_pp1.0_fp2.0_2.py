import types
types.MethodType(unresolved_table_write,c)
c.write("test.mdb")
</code>
To be clear: I don't need to use the data written to the table, I just need to open the mdb file and confirm that the table has been created. 
Does anyone know what I could do to resolve this issue? 


A:

Actually, I think your code should work as is.  However I made a small change and it did work.  I changed
<code>types.MethodType(unresolved_table_write,c)
</code>
to
<code>types.MethodType(unresolved_table_write,c,c)
</code>
I'm not sure what is happening here, but it seems to apply the function to the object you are creating, which is a class instance, not just a class.
For what it's worth, I tried just changing the code to be:
<code>c.unresolved_table_write('TestFile.mdb')
</code>
and I got the error:
<code>AttributeError: '_Table' object has
