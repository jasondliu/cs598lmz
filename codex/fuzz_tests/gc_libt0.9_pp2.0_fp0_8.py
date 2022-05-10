import gc, weakref
wref_to_ros_node_obj=weakref.ref(ros_node_obj)
</code>
Now, the reference to my object won't be held by the main program anymore, and I hope the garbage collector will reclaim it. 
Is this a viable way of deleting my object? Are there better approaches, perhaps some way to delete the object without ever letting it be assigned as a global
variable? Does the weakref package do what I think it does?
If I then want to access that same object in the original way, I would do so
(I think) by using <code>wref_to_ros_node_obj()</code> rather than <code>ros_node_obj</code>.
If it goes out of scope, the <code>weakref</code> object would go out of scope as well.


A:

According to this link:
<blockquote>
<p>Before being garbage-collected, weak references have to be explicitly removed from their container.</p>
</blockquote>
The last part does not make sense, but I think its trying to say that an object that is a <code>
