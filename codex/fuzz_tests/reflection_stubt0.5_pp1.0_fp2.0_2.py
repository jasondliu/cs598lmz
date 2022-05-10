fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

def fn():
    1 / 0

fn.__code__ = 'foo'
fn()

def fn():
    1 / 0

fn.__code__ = 1
fn()

def fn():
    1 / 0

fn.__code__ = None
fn()

def fn():
    1 / 0

fn.__code__ = {'co_name': 'foo', 'co_argcount': 0}
fn()

def fn():
    1 / 0

fn.__code__ = {'co_name': 'foo', 'co_argcount': 0, 'co_code': 'a'}
fn()

def fn():
    1 / 0

fn.__code__ = {'co_name': 'foo', 'co_argcount': 0, 'co_code': ''}
fn()

def fn():
    1 / 0

fn.__code__ = {'co_name': 'foo', 'co_argcount': 0, 'co_code': '\x01'}
fn()

def
