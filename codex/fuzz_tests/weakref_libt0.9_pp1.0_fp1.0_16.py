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


class Column(object):
    """Base class for columns.

    Defines methods for providing the following:
        name: the columns internal name.
        label: (string) the name of the column that is presented to the end-user.
        column_type: (string) the type of the column, string or number.
        description: (string) explanation of the column.

    Illustrates that the following variables can be
