import gc, weakref, time
from logging import getLogger
from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.utils import PyPdfError
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from PyPDF2.generic import TextStringObject, NameObject
from PyPDF2.utils import PdfReadError
from . import pdf_utils
from . import pdf_merge
from . import pdf_split
from . import pdf_watermark
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import fonts
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY


