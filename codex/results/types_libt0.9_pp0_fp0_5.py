import types
types.MethodType(copyreg.dispatch_table,None,DefaultMixin)
types.MethodType(copyreg.dispatch_table,None,OrderedDict)
types.MethodType(copyreg.dispatch_table,None,OrderedDictMixin)
types.MethodType(copyreg.dispatch_table,None,Bag)
types.MethodType(copyreg.dispatch_table,None,CountingSet)
types.MethodType(copyreg.dispatch_table,None,Table)
types.MethodType(copyreg.dispatch_table,None,Meta)
</code>


A:

Pickling fails due to a lower level problem. <code>types.MethodType</code> objects cannot be pickled:
<code>&gt;&gt;&gt; import pickle
&gt;&gt;&gt; pickle.loads(pickle.dumps(types.MethodType))
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
_pickle.Pickling
