fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_name == '<lambda>'

# __getstate__
class C():
    def __getstate__(self):
        return None

x = C()
