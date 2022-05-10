from types import FunctionType
list(FunctionType(j.core.portal.active.server.app.__code__.co_consts[0]).__code__.co_consts)

from jinja2 import Environment
env = Environment()
from jinja2.exceptions import TemplateNotFound
from jinja2 import Template
from jinja2.runtime import Undefined
from jinja2.environment import TemplateModule
from jinja2.loaders import BaseLoader, DictLoader, PackageLoader, FileSystemLoader
from jinja2.utils import open_if_exists
from jinja2.bccache import BytecodeCache, FileSystemBytecodeCache
from jinja2.compiler import CodeGenerator
from jinja2.environment import Environment
from jinja2.exceptions import TemplateNotFound, TemplateSyntaxError, TemplateAssertionError, TemplateError, UndefinedError, SecurityError, TemplatesNotFound
from jinja2.filters import FILTERS
from jinja2.lexer import TokenStream, DEFAULT_BLOCK_START_STRING, DEFAULT_BLOCK_END
