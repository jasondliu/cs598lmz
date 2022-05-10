from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

import imp
imp.reload(packstruct)

from packstruct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

from packstruct import Struct
s = Struct('>QQQ')
s.size


import packstruct
reload(packstruct)
from packstruct import Struct
s = Struct('>QQQ')
s.size

import packstruct
reload(packstruct)
from packstruct import Struct
s = Struct('>QQQ')
s.size

import packstruct
reload(packstruct)
from packstruct import Struct
s = Struct('>QQQ')
s.size

import packstruct
reload(packstruct)
from packstruct import Struct
s = Struct('>QQQ')
s.size

import packstruct
reload(packstruct)
from packstruct import Struct
s = Struct('>QQQ')
s.size

import packstruct
reload(packstruct)
