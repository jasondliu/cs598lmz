import mmap

import numpy as np

from .. import util
from .. import ndimage

from .. import _template_generator
from .. import _template_generator_c

def _generate_template(data, template_shape, template_step, template_start, template_end,
                       template_dtype, template_offset):
    data = np.ascontiguousarray(data)

    if data.ndim != 3:
        raise ValueError("data must be three dimensional")

    if np.issubdtype(data.dtype, np.complexfloating):
        raise ValueError("data must be real")

    if len(template_shape) != 2:
        raise ValueError("template_shape must be two dimensional")

    if len(template_step) != 2:
        raise ValueError("template_step must be two dimensional")

    if len(template_start) != 2:
        raise ValueError("template_start must be two dimensional")

    if len(template_end) != 2:
        raise ValueError("template_end must be two dimensional")

