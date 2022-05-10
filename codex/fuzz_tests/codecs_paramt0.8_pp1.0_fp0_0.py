import codecs
codecs.register_error(
    'strict', codecs.lookup_error('strict')
)

import os

exec(open(os.path.expanduser('~/.emscripten'), 'r').read())

SETTINGS = {
    'INCLUDES': [
        os.path.join(EMSCRIPTEN_ROOT, 'system', 'include'),
    ],
    'CFLAGS': [
        '-Wall',
        '-Wextra',
        '-Werror',
        '-O2',
        #'-std=gnu99',
        '-ffast-math',
        '-ftree-vectorize',
        '-fno-math-errno',
        '-fno-finite-math-only',
        '-fno-signed-zeros',
        '-fno-trapping-math',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-Wno-c++11-extensions',
    ],
    'DEFINES': [
    ],

