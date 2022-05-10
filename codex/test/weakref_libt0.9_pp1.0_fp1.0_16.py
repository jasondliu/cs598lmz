import weakref
from django.conf import settings
from django.dispatch import receiver
from django.utils.functional import curry
from cc3.excelexport.models import ExcelExportSheet, ExcelSheet
from cc3.excelexport.signals import excel_export_pre_save, excel_export_post_save, excel_export_post_delete


def describe(name, dictionary):
    """Describes model sheet format by name."""
    def decorator(cls):
        """Function decorator."""
        dictionary[name] = cls
        setattr(cls, 'describe', staticmethod(lambda: name))
        return cls
    return decorator


