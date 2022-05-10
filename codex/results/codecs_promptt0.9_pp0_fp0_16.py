import codecs
# Test codecs.register_error('test_replace_replace',test_replace_replace)
# codecs.register_error('test_replace_replace',test_replace_replace)
# codecs.register_error('test_replace_ignore',test_replace_ignore)
# codecs.register_error('test_replace_strict',test_replace_strict)
# codecs.register_error('test_replace_html',test_replace_html)
# codecs.register_error('test_replace_xmlattr',test_replace_xmlattr)


def corrupt_replace(repl_str):
    def handle_exception(ex):
        def get_pos(ignored):
            return (ex.start, ex.end)
        setattr(ex,'start',0)
        setattr(ex,'end',len(ex.object))
        # setattr(ex,'reason','')
        return (repl_str, get_pos)
    return handle_exception

def test_replace_replace(ex):
    def get_pos(ignored):
        return (ex.start, ex.end)
