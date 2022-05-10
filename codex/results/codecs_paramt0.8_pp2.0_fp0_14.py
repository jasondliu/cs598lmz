import codecs
codecs.register_error("strict", codecs.ignore_errors)

from docutils.transforms.substitutions import NormalizeWhitespace
from docutils.nodes import raw, comment

from .utils import name_re, ref_re
from .utils.autoimport import _AutoImportMethod
from .utils.external import _ExternalMethod
from .utils.path import _PathMethod
from .utils import dict_, log


def _get_mime_data(self, name):
	data = mimeformat.get_data(name)
	return data


###  Constants  ###

SECTION_DEPTH = 7
SECTION_STYLE = [
	"Part {index}: {title}",
	"Chapter {index}: {title}",
	"Section {index}: {title}",
	"Subsection {index}: {title}",
	"Subsubsection {index}: {title}",
	"Subsubsubsection {index}: {title}",
	"Subsubsubsubsection {index}: {title}"
]

FORMULA_OUTPUT_FORMAT = "
