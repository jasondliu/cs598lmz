from bz2 import BZ2Decompressor
BZ2Decompressor('')
"
);

// 2.1.2.1.8
add_library_check!(
    "@.so",
    "
from ctypes import cdll
cdll.LoadLibrary('')
"
);

// 2.1.2.1.9
// 2.1.2.1.10
add_library_check!(
    "@.dylib",
    "
from ctypes import cdll
cdll.LoadLibrary('')
"
);

// 2.1.2.1.11
add_library_check!(
    "@.dll",
    "
from ctypes import WinDLL
WinDLL('')
"
);

// 2.1.2.1.12
add_library_check!(
    "@.lib",
    "
from ctypes import WinDLL
WinDLL('')
"
);

// 2.1.2.1.13
add_library_check!(
    "@.dll",
    "
from ctypes import WinDLL
WinDLL('')
