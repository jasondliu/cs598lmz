import weakref, warnings
import matplotlib.colors as mcolors


class BaseFillSymbol(ISymbol):
    """Base fill symbol class.
    
    :param color: Symbol color
    :type color: tuple, list or QColor
    """
    
    def __init__(self, color=None):
        self.__color = QColor()
        
        if color is not None:
            self.__color = qcolor(color)
            
        self.setSymbolColor(color)
    
    def symbolCode(self):
        return QgsSymbolV2.FILL
    
    def symbolName(self):
        return QgsSymbolLayerV2Utils.symbolLayerType(self)
    
    def setSymbolColor(self, color):
        self.__color = qcolor(color)
    
    def symbolColor(self):
        return self.__color
    
    def defaultColor(self):
        return QColor()


class SimpleFillSymbol(BaseFillSymbol, SymbolLayer):
    """Simple fill symbology object.
