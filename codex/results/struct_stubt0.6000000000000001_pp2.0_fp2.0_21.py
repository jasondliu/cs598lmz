from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('b')

import pickle
pickle.dumps(s)
</code>
Или поставьте ограничение на возможность сериализации таких объектов:
<code>class Struct(Struct):
    def __getstate__(self):
        raise TypeError('Unserializable object')
</code>

