fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_firstlineno = 2
fn.__code__.co_code = 'd\x00S'
fn.__code__.co_flags = inspect.CO_GENERATOR
globals()['fn'] = fn
fn()
EOF

    ./python -c "$script"

    script="$(cat << EOF
import sys, inspect
def fn():
    def fn():
        yield
    return fn
fn = fn()
gi = (i for i in ())
fn.gi_code = gi.gi_code = type(lambda: None)()
fn.gi_code.co_firstlineno = 2
fn.gi_code.co_code = 'd\x00S'
fn.gi_code.co_flags = inspect.CO_GENERATOR
globals()['fn'] = fn
fn()
EOF
)"

    ./python -c "$script"

}

function test_co_valuedict() {
    # Issue #29217: don
