fn = lambda: None
gi = (i for i in ())
fn.__code__ = [(lambda: None)]
gi.gi_code = fn.__code__
gi.gi_frame = {}
gi.gi_running = []
gi.gi_frame.f_locals = {}
del fn, gi


def add_context(context, pos):
    import types
    import opcode
    import logging
    ALL_INSTRUCTIONS = {}

    def save_opcode(name):
        def decorate(func):
            def wrapper(self, *args, **kwargs):
                pos = ALL_INSTRUCTIONS[self.lasti]
                retval = func(self, *args, **kwargs)
                logging.debug('%s (%s): %s' % (name, pos, args[0].co_code[pos:pos+3]))
                data = context['data']
                if name == 'RETURN_VALUE':
                    data.append({'event': 'return value', 'value': repr(args[0])})
                elif name == 'STORE_NAME':
                    data.append({'event': 'store name', 'name': args[
