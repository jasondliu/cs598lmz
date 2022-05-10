import ctypes
ctypes.cast( self );
</code>
And there is no std::dynamic_cast operator, that I know of for python,
unless I am mixing up things. So, my guess would be, that you need to directly work with the <code>&lt;pyside_dynamic_metaobject&gt;</code> object, or write similar operator yourself.

