import weakref

class _Processor(object):
    """Processor.

    A Processor is an object that performs some task on a message.
    It has a priority, and can optionally have other Processors as
    parents, or be the child of one or more Processors.

    If a child Processor is added to this Processor, it will be
    processed before this Processor.

    If a parent Processor is added to this Processor, it will be
    processed only after this Processor.

    If a Processor is added as both a child and a parent, the
    Processor will be processed in the natural order.

    Generally, Processors will be added as children, so that they are
    processed before this Processor.

    A Processor must define a _process() method. This method is
    called with a message as the argument and should return the
    message.

    If a Processor has a _preprocess_hook method, this will be
    executed before the _process() method. The same is true for
    _postprocess_hook.

    A Processor can optionally define a _get_priority() method, which
    should return a numeric priority value. This value is
