import _struct
# Test _struct.Struct.

# Test format string

try:
    _struct.Struct('c')
except TypeError:
    print('SKIP')
    raise SystemExit

try:
    _struct.Struct('!')
except _struct.error:
    print('SKIP')
    raise SystemExit

try:
    _struct.Struct('!I')
except _struct.error:
    print('SKIP')
    raise SystemExit

try:
    _struct.Struct('!Ih')
except _struct.error:
    print('SKIP')
    raise SystemExit

try:
    _struct.Struct('!Ihh')
except _struct.error:
    print('SKIP')
    raise SystemExit

try:
    _struct.Struct('!Ihhi')
except _struct.error:
    print('SKIP')
    raise SystemExit

try:
    _struct.Struct('!IhhiI')
except _struct.error:
    print('SKIP')
    raise SystemExit

try:
    _struct.Struct('!Ihhi
