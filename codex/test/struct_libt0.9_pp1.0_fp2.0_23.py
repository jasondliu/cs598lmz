import _struct
from hypothesis.strategies import composite, integers
from hypothesis.strategies import lists, sampled_from, tuples, text

from .strategies import sequences, sequences_no_duplicates


def struct_functions():
    return tuples(
        sampled_from(
            getattr(
                _struct,
                attr,
            )
            for attr in dir(_struct)
            if attr.isupper() and len(attr) == 1
        ),
        integers(),
        integers(),
    )


@composite
def struct_struct(draw):
    function, offset, length = draw(struct_functions())
    template = f"{function}{length}"
    packed = _struct.pack(template, *draw(lists(integers(), min_size=length)))
    endianness = ">" if function == _struct.calcsize(template) >> 2 else "<"
    try:
        return offset, _struct.unpack(endianness + template, packed)[0]
    except _struct.error:
        return offset, None



