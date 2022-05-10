import _struct
import _stream
import _exception
import _string
import _json
import _object
import _array
import _hash
import _regexp
import _function
import _class
import _module
import _package
import _eval
import _file
import _process
import _system
import _native

class VM(_object.Object):
    def __init__(self):
        super(VM, self).__init__()

        self.version = "0.0.1"
        self.argv = _array.Array()
        self.env = _hash.Hash()
        self.stdin = None
        self.stdout = None
        self.stderr = None

        self.class_map = {
            "object": _object.Class,
            "array": _array.Class,
            "hash": _hash.Class,
            "regexp": _regexp.Class,
            "function": _function.Class,
            "class": _class.Class,
            "module": _module.Class,
            "package": _package.Class,
