from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
</code>
This (instantiation) isn't guaranteed to be safe, but it's what the standard library does (and it's probably not something users can easily influence, as they are likely not directly instantiating the <code>Struct</code> class at all).
(<code>BytesIO</code> has exactly the same case as <code>Struct</code>)

