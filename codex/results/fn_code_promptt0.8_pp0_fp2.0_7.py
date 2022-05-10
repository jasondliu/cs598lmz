fn = lambda: None
# Test fn.__code__.co_argcount works with iter
def foo(*i):
    return i
"""

    def test_window(self, space):
        w_res = space.execute("""
            return [
                window.document.title,
                window.name,
                window.length,
                window.parent.location.pathname,
                window.frameElement.nodeName,
                window.top.history.length,
                window.top.location.pathname,
                window.top.parent.location.pathname,
                window.top.self.location.pathname,
                window.top.window.location.pathname,
                window.top.frames[0].location.pathname,
                window.top.frames.length,
            ]
            """)
        assert space.is_true(space.eq(
            w_res,
            space.newlist([
                space.newtext("W_HTMLDocument"),
                space.newtext(""),
                space.newint(0),
                space.newtext("/test_window.html"),
                space.newtext("
