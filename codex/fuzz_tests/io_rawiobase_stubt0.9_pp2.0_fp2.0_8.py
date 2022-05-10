import io
class File(io.RawIOBase):
    ...

class RawIO(io.RawIOBase):
    ...
</code>
Later, in <code>test_io</code>:
<code># make sure that the io.RawIOBase class is in fact a base
# class of any IO class.
import io
def assertIsSubclass(sub, sup, msg=None):
    ...
</code>

