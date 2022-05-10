import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, weakref

def callback(obj):
    print "deleted", obj

for n in range(1000):
    if n == 16:
        gc.collect()
    ref = weakref.ref(n, callback)
</code>
Gives:
<code>gc: collectable &lt;5002&gt;
gc: collectable &lt;5003&gt;
gc: collectable &lt;5004&gt;
gc: collectable &lt;5005&gt;
gc: collectable &lt;5006&gt;
gc: collectable &lt;5007&gt;
gc: collectable &lt;5008&gt;
gc: collectable &lt;5009&gt;
gc: collectable &lt;5010&gt;
deleted 5010
gc: collectable &lt;5011&gt;
deleted 5011
gc: collectable &lt;5012&gt;
deleted 5012
gc: collectable &lt;5013&gt;
deleted 5013
gc: collectable &lt;5014&gt;

