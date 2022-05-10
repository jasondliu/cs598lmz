from _struct import Struct
s = Struct.__new__(Struct)
#s._map = 'hi'
s.__init__('hi')
data = 'abc' #(12, 45)
s.pack(data)
</code>


A:

You're using <code>Struct.__new__()</code> when you really want to call <code>Struct()</code>, which calls <code>Struct.__new__()</code> for you, then initializes the instance it returns before returning the initialized instance.
Use <code>s = Struct('hi')</code> instead, and the pack method will become available.
From the documentation:
<blockquote>
<p>This factory function returns a built-in object. These objects have
  different characteristics: they are called like built-in functions but
  their type is ‘type’ rather than ‘function’, they support the
  ‘<strong>call</strong>’ method, but not the ‘<strong>getattr</strong>’ method, their globals are not
  the module’s globals, they have a <code>&lt;code&gt;__module__
