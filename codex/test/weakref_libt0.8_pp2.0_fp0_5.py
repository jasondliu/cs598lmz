import weakref

from sphinx.util import logging

from sphinx_markdown_parser.parser import MarkdownParser
from sphinx_markdown_parser.transform import AutoStructify
from sphinx_markdown_parser.transform import MarkdownInclude
from sphinx_markdown_parser.directives import code_block

from docutils import nodes
from docutils.core import publish_string

from sphinx.util.nodes import NodeMatcher
from sphinx.util.osutil import ensuredir
from sphinx.util.fileutil import copy_asset
from sphinx.util.osutil import copyfile
from sphinx.util.texescape import tex_escape_map
from sphinx.util.images import guess_mimetype
from sphinx.util.console import bold, darkgreen, purple, brown, red
from sphinx.util.i18n import find_catalog_source_files
