fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
'}
try 1 '\{
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
'}
try 1 '\{
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
'}

try 1 '\{
def fn():
    pass
fn.__code__ = (i for i in ())
fn()
'}
try 1 '\{
def fn():
    pass
fn.__code__ = (i for i in ())
fn()
'}
try 1 '\{
def fn():
    pass
fn.__code__ = (i for i in ())
fn()
'}

try 2 '\{
def foo():
    yield
def fn():
    pass
fn.__code__ = foo()
fn()
'}
try 2 '\{
def foo():
    yield
def fn():
    pass
fn.__code__ = foo()
fn()
'}
try 2 '\{

