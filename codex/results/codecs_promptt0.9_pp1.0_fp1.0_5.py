import codecs
# Test codecs.register_error function
import re, base64

# To print a bitmap as an XBM file
import array

# Generating random letters and lines
from random import choice, randint
import random

# Getting PostScript
from reportlab.graphics.shapes import Group, Drawing, Line, Rect, RoundedRect, Ellipse, Circle, Wedge
from reportlab.graphics.shapes import Polygon, PolyLine, Flowable
from reportlab.graphics.shapes import String, Image,arc
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

# Using the Results of a Superscript or Subscript
from reportlab.lib.textsplit import TextSplitter

# Using Text Objects
from reportlab.pdfbase import pdfmetrics
from reportlab
