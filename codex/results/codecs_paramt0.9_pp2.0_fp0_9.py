import codecs
codecs.register_error('noRepl', codecs.ignore_errors)

from datetime import datetime
from unidecode import unidecode
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.layout import LTFigure
from pdfminer import high_level

from . import plenarprotokoll
from . import utils


class Reader():
    """Holds all commandline options and arguments.

    Provides methods for

    * introspecting commandline arguments,
    * control of flow based on arguments,
   
