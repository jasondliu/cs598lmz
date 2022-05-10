import mmap
from mpatches import PathPatch
from matplotlib.transforms import Bbox
from matplotlib.text import TextPath
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.font_manager import FontProperties
from matplotlib.collections import LineCollection
def make_test_pdf(filename):
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
    c = canvas.Canvas(filename)
    c.setFont('Arial', 10)
    
    barcode = '*C1041412061046708*'
    barcode = barcode.encode('utf-8').decode('utf-8-sig')
    c.drawString(35, 725, barcode[0:16])
    c.drawString(35, 700, barcode[16:32])
    c.drawString(35, 675, barcode[32:48])
    c.drawString(35, 650, barcode[48:64])
    
    c.drawString(35, 630, '
