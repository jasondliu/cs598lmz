import weakref
__all__ = ['Widget', 'WidgetError', 'SerializationError', 'StyleError', 'TemplateError', 'WidgetDisabled', 'WidgetShowError', 'WidgetLabelError', 'WidgetDisplayError', 'WidgetTemplateError', 'WidgetTemplateNotFound', 'WidgetOnFormError', 'WidgetFormInvalid']

class Widget(object):
    """
    A base class for all widgets.
    """
    __slots__ = ('_obj', '_name', '_value', '_show', '_required', '_default', '_kw', '_template', '_children', '_parent', '_form', '_disabled', '_error', '_label')
    _children = None
    _parent = None
    _form = None
    _default = None

