import types
types.ModuleType

from django.conf import settings
DEBUG = socket.gethostname() == settings.INTERNAL_IPS[0]
if settings.DEBUG is True:
    DEBUG = True
from django.conf import settings
from django.template import TemplateSyntaxError, Node, Variable
from django.template.loader import render_to_string, get_template
from django.template import Context, Template, Library


def _apply(func, name, targs, kwargs, nodelist):
    def render(context):
        try:
            v = []
            v.append(_lookup(context, name))
            context.update(_aggregate_dict(*v))
            r = nodelist.render(context)
            context.pop()
            return r
        except StandardError, e:
            info = sys.exc_info()
            if DEBUG:
                import cgitb; cgitb.handler()
                print >> sys.stderr, "ERROR in TemplateAtomizer:"
                import traceback
                traceback.print_exc()
            else:
                return
