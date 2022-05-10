import mmap
from io import BytesIO
from lxml import etree
from xlwt import Workbook, easyxf, Formula
import datetime
import time
from openerp.addons.report_xls.report_xls import report_xls
from openerp.addons.report_xls.utils import rowcol_to_cell, _render
from .dym_report_penjualan_valas import dym_report_penjualan_valas_print
from openerp.tools.translate import translate
import logging
_logger = logging.getLogger(__name__)

class dym_report_penjualan_valas_print_xls(dym_report_penjualan_valas_print):

    def __init__(self, cr, uid, name, context):
        super(dym_report_penjualan_valas_print_xls, self).__init__(
            cr, uid, name, context=context)
        move_line_obj = self.pool.get('account.move.line')
        self
